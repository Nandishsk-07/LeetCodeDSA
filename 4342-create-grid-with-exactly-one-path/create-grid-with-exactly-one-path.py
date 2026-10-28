class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = [["#"] * n for _ in xrange(m)]
        for j in xrange(n):
            grid[0][j] = "."
        for i in xrange(m):
            grid[i][n - 1] = "."
        return ["".join(row) for row in grid]
        