class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in xrange(m):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][n - 1] == 0:
                dfs(r, n - 1)
        for c in xrange(n):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[m - 1][c] == 0:
                dfs(m - 1, c)
        closed_islands = 0
        for r in xrange(1, m - 1):
            for c in xrange(1, n - 1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    closed_islands += 1
        return closed_islands
        