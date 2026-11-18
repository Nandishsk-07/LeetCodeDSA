class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        divisors = [[] for _ in xrange(n + 1)]
        for L in xrange(2, n + 1):
            for d in xrange(1, L // 2 + 1):
                if L % d == 0:
                    divisors[L].append(d)
        INF = float('inf')
        cost = [[INF] * n for _ in xrange(n)] 
        for i in xrange(n):
            for j in xrange(i + 1, n):
                L = j - i + 1
                best_sub_cost = INF
                for d in divisors[L]:
                    changes = 0
                    m = L // d
                    for r in xrange(d):
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
        for p in xrange(1, k + 1):
            curr_dp = [INF] * (n + 1)
            max_j = n - 2 * (k - p)
            for j in xrange(2 * p, max_j + 1):
                for i in xrange(2 * (p - 1), j - 1):
                    val = prev_dp[i] + cost[i][j - 1]
                    if val < curr_dp[j]:
                        curr_dp[j] = val
            prev_dp = curr_dp
        return prev_dp[n]
        