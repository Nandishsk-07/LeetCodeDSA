class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for char_s in s:
            for j in xrange(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]
        