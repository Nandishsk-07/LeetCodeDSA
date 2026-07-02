class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        min_damage = [[float('inf')] * n for _ in xrange(m)]
        start_damage = grid[0][0]
        min_damage[0][0] = start_damage
        q = deque([(0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return (health - min_damage[r][c]) >= 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    next_damage = min_damage[r][c] + weight
                    if next_damage < min_damage[nr][nc]:
                        min_damage[nr][nc] = next_damage
                        if weight == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))
        return (health - min_damage[m - 1][n - 1]) >= 1
        