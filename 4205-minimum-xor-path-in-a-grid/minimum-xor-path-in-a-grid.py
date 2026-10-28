class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[set() for _ in xrange(n)] for _ in xrange(m)]
        dp[0][0].add(grid[0][0])
        for i in xrange(m):
            for j in xrange(n):
                val = grid[i][j]
                if i > 0:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ val)
                if j > 0:
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ val)
        return min(dp[m - 1][n - 1])
            
        