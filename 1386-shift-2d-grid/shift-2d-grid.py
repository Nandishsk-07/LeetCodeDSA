class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        k = k % total_elements
        result = [[0] * n for _ in xrange(m)]
        for r in xrange(m):
            for c in xrange(n):
                flat_idx = r * n + c
                new_flat_idx = (flat_idx + k) % total_elements
                new_r = new_flat_idx // n
                new_c = new_flat_idx % n
                result[new_r][new_c] = grid[r][c]
        return result
        