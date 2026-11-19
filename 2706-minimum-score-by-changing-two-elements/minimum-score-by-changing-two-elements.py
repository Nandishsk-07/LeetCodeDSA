class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return min(
            nums[-1] - nums[2],
            nums[-3] - nums[0],
            nums[-2] - nums[1]
        )
        