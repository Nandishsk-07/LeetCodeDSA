class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        squares = [x * x for x in nums]
        squares.sort()
        neg_count = n // 2
        return sum(squares[neg_count:]) - sum(squares[:neg_count])
        