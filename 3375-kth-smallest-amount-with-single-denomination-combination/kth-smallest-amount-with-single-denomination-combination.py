class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        for r in range(1, n + 1):
            sign = 1 if r % 2 == 1 else -1
            for combo in combinations(coins, r):
                lcm_val = combo[0]
                for x in combo[1:]:
                    lcm_val = (lcm_val * x) // math.gcd(lcm_val, x)
                subsets.append((lcm_val, sign))        
        def count(x: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (x // lcm_val)
            return total
        low = 1
        high = min(coins) * k
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        