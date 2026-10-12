class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 1000000007
        bit_counts = [0] * 30
        for x in nums:
            for b in xrange(30):
                if (x >> b) & 1:
                    bit_counts[b] += 1
        ans = 0
        for _ in xrange(k):
            val = 0
            for b in xrange(30):
                if bit_counts[b] > 0:
                    val |= (1 << b)
                    bit_counts[b] -= 1
            ans = (ans + val * val) % MOD
        return ans
        