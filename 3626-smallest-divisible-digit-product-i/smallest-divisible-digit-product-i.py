class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        x = n
        while True:
            prod = 1
            for digit in str(x):
                prod *= int(digit)
            if prod % t == 0:
                return x
            x += 1
        