class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, ch in enumerate(s):
            weight = 26 - (ord(ch) - ord('a'))
            total += (i + 1) * weight
        return total
        