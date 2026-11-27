class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for m in range(f, max_factor + 1, f):
                    multiples_count[f] += freq[m]
        min_price = min(p for _, p in items)
        dp = [-1] * (budget + 1)
        dp[0] = 0
        for f, p in items:
            if p > budget:
                continue
            val = multiples_count[f]
            for c in range(budget, p - 1, -1):
                if dp[c - p] != -1 and dp[c - p] + val > dp[c]:
                    dp[c] = dp[c - p] + val
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                total = dp[c] + (budget - c) // min_price
                if total > ans:
                    ans = total
        return ans
        