class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        opt1 = j + 1
        opt2 = n - i
        opt3 = (i + 1) + (n - j)
        return min(opt1, opt2, opt3)
        