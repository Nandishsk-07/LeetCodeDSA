class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        squares = [x * x for x in nums]
        squares.sort()
        neg_count = n // 2
        return sum(squares[neg_count:]) - sum(squares[:neg_count])
        