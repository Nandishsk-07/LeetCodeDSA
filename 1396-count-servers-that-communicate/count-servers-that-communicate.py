class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        row_counts = [0] * m
        col_counts = [0] * n
        for r in xrange(m):
            for c in xrange(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        communicating_servers = 0
        for r in xrange(m):
            for c in xrange(n):
                if grid[r][c] == 1 and (row_counts[r] > 1 or col_counts[c] > 1):
                    communicating_servers += 1
        return communicating_servers
        