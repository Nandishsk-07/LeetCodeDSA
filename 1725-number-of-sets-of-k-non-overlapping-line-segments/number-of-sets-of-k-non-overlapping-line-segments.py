class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        N = n + k - 1
        R = 2 * k
        if R > N or R < 0:
            return 0
        num = 1
        den = 1
        for i in xrange(1, R + 1):
            num = (num * (N - i + 1)) % MOD
            den = (den * i) % MOD
        return (num * pow(den, MOD - 2, MOD)) % MOD
        