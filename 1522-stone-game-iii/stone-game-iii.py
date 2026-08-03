class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)   
        for i in xrange(n - 1, -1, -1):
            max_advantage = float('-inf')
            take_sum = 0       
            for k in xrange(1, 4):
                if i + k - 1 < n:
                    take_sum += stoneValue[i + k - 1]
                    max_advantage = max(max_advantage, take_sum - dp[i + k])
            dp[i] = max_advantage       
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
        