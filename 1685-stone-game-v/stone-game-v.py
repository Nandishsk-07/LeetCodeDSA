class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for idx in range(n):
            prefix[idx + 1] = prefix[idx] + stoneValue[idx] 
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == j:
                return 0
            total = prefix[j + 1] - prefix[i]
            max_score = 0
            for k in range(i, j):
                left_sum = prefix[k + 1] - prefix[i]
                right_sum = total - left_sum
                if left_sum < right_sum:
                    if left_sum * 2 <= max_score:
                        continue
                    max_score = max(max_score, left_sum + dp(i, k))
                elif right_sum < left_sum:
                    if right_sum * 2 <= max_score:
                        continue
                    max_score = max(max_score, right_sum + dp(k + 1, j))
                else:
                    max_score = max(max_score, left_sum + max(dp(i, k), dp(k + 1, j)))
            return max_score
        return dp(0, n - 1)
        