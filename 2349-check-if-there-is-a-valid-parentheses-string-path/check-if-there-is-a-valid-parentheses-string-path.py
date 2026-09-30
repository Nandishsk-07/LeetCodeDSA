class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_len = m + n - 1
        if total_len % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False    
        max_bal = total_len // 2
        visited = set()
        def dfs(r: int, c: int, bal: int) -> bool:
            if bal < 0 or bal > max_bal:
                return False
            if (m - 1 - r) + (n - 1 - c) < bal:
                return False                
            if r == m - 1 and c == n - 1:
                return bal == 0     
            state = (r, c, bal)
            if state in visited:
                return False
            visited.add(state)
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < m and nc < n:
                    delta = 1 if grid[nr][nc] == '(' else -1
                    if dfs(nr, nc, bal + delta):
                        return True
            return False
        return dfs(0, 0, 1)