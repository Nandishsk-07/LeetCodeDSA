class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        return [x for x in xrange(min_val, max_val + 1) if x not in num_set]
        