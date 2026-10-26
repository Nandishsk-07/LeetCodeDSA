class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] > 0:
                    island_sum = 0
                    stack = [(i, j)]
                    island_sum += grid[i][j]
                    grid[i][j] = 0
                    while stack:
                        r, c = stack.pop() 
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))
                    if island_sum % k == 0:
                        ans += 1      
        return ans
        