class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        drops = 0
        n = len(nums)
        for i in xrange(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
            if drops > 1:
                return False
        return True 

        