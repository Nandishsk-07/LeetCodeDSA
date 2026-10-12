class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        bit_counts = [0] * 30
        for x in nums:
            for b in range(30):
                if (x >> b) & 1:
                    bit_counts[b] += 1
        ans = 0
        for _ in range(k):
            val = 0
            for b in range(30):
                if bit_counts[b] > 0:
                    val |= (1 << b)
                    bit_counts[b] -= 1
            ans = (ans + val * val) % MOD
        return ans
        
        