class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_idx = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_idx], nums[i] = nums[i], nums[last_non_zero_idx]
                last_non_zero_idx += 1
        