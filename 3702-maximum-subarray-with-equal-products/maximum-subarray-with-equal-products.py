class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        max_len = 1
        for i in xrange(n):
            prod = 1
            g = 0
            l = 1
            for j in xrange(i, n):
                val = nums[j]
                prod *= val
                g = gcd(g, val)
                l = (l * val) // gcd(l, val)
                if prod == l * g:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                elif prod > l * g:
                    break
        
        return max_len