class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        for i in xrange(len(nums)):
            val = nums[i]
            if val != i:
                if ans == -1:
                    ans = val & i
                else:
                    ans &= (val & i)
        return 0 if ans == -1 else ans
        