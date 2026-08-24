class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in xrange(1, n):
            prefix[i] = prefix[i - 1] + stones[i]   
        dp = prefix[-1]
        for i in xrange(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
        return dp
        