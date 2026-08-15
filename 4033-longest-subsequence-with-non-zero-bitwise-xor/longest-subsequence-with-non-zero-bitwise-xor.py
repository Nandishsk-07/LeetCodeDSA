class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        all_zeros = True
        for num in nums:
            total_xor ^= num
            if num != 0:
                all_zeros = False
        if all_zeros:
            return 0
        if total_xor != 0:
            return len(nums)
        return len(nums) - 1