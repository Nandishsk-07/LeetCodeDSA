class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 0
        for j in xrange(1, n + 1):
            step_cost = costs[j - 1]
            min_prev = dp[j - 1] + 1
            if j >= 2:
                min_prev = min(min_prev, dp[j - 2] + 4)
            if j >= 3:
                min_prev = min(min_prev, dp[j - 3] + 9)
            dp[j] = step_cost + min_prev
        return dp[n]
        