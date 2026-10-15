class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = 0
        for i in xrange(n):
            seen = set()
            for j in xrange(i, n):
                seen.add(nums[j])
                total_sum += len(seen) * len(seen)
        return total_sum
        