class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L // 2 + 1):
                if L % d == 0:
                    divisors[L].append(d)
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]      
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best_sub_cost = INF
                for d in divisors[L]:
                    changes = 0
                    m = L // d
                    for r in range(d):
                        left = i + r
                        right = i + r + (m - 1) * d
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < best_sub_cost:
                        best_sub_cost = changes
                cost[i][j] = best_sub_cost
        prev_dp = [INF] * (n + 1)
        prev_dp[0] = 0
        for p in range(1, k + 1):
            curr_dp = [INF] * (n + 1)
            max_j = n - 2 * (k - p)
            for j in range(2 * p, max_j + 1):
                for i in range(2 * (p - 1), j - 1):
                    val = prev_dp[i] + cost[i][j - 1]
                    if val < curr_dp[j]:
                        curr_dp[j] = val
            prev_dp = curr_dp
        return prev_dp[n]