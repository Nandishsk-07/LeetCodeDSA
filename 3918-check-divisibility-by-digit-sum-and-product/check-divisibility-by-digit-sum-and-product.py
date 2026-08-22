class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_digits = 0
        prod_digits = 1
        for digit in str(n):
            d = int(digit)
            sum_digits += d
            prod_digits *= d
        total_divisor = sum_digits + prod_digits
        return n % total_divisor == 0
        