class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc = 1
        dec = 1
        max_len = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            if inc > max_len:
                max_len = inc
            if dec > max_len:
                max_len = dec
        return max_len
        