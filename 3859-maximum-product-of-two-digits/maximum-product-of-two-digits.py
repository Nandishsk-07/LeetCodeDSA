class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted(str(n))
        return int(digits[-1]) * int(digits[-2])
        