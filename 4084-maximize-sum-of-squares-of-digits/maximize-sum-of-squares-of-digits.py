class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum < 1 or sum > 9 * num:
            return ""
        q, r = divmod(sum, 9)
        zeros = num - q - (1 if r > 0 else 0)
        parts = ["9" * q]
        if r > 0:
            parts.append(str(r))
        if zeros > 0:
            parts.append("0" * zeros)
        return "".join(parts)
        