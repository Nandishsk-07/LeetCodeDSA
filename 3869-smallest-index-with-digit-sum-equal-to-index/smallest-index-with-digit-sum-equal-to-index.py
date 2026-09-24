class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            digit_sum = 0
            temp = nums[i]
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            if digit_sum == i:
                return i
        return -1
        