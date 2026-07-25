class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = sorted(str(n))
        return int(digits[-1]) * int(digits[-2])
        