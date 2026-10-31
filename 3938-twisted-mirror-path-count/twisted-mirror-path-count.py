class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        
        # nxt[r][c][d] stores (target_r, target_c) or None
        # d = 0 represents entering moving RIGHT
        # d = 1 represents entering moving DOWN
        nxt = [[[None, None] for _ in range(n)] for _ in range(m)]
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        
        # Process cells by decreasing sum of coordinates (r + c)
        for s in range(m + n - 2, -1, -1):
            for r in range(max(0, s - (n - 1)), min(m, s + 1)):
                c = s - r
                
                if grid[r][c] == 1:
                    # Mirror cell: resolve reflection exits
                    # 1. Entered DOWN (d = 1) -> turns RIGHT to (r, c + 1)
                    if c + 1 < n:
                        if grid[r][c + 1] == 0:
                            nxt[r][c][1] = (r, c + 1)
                        else:
                            nxt[r][c][1] = nxt[r][c + 1][0]
                    else:
                        nxt[r][c][1] = None
                        
                    # 2. Entered RIGHT (d = 0) -> turns DOWN to (r + 1, c)
                    if r + 1 < m:
                        if grid[r + 1][c] == 0:
                            nxt[r][c][0] = (r + 1, c)
                        else:
                            nxt[r][c][0] = nxt[r + 1][c][1]
                    else:
                        nxt[r][c][0] = None
                else:
                    # Empty cell: calculate paths if not the destination
                    if r == m - 1 and c == n - 1:
                        continue
                        
                    ways = 0
                    
                    # Option 1: Move RIGHT
                    if c + 1 < n:
                        target = (r, c + 1) if grid[r][c + 1] == 0 else nxt[r][c + 1][0]
                        if target is not None:
                            ways = (ways + dp[target[0]][target[1]]) % MOD
                            
                    # Option 2: Move DOWN
                    if r + 1 < m:
                        target = (r + 1, c) if grid[r + 1][c] == 0 else nxt[r + 1][c][1]
                        if target is not None:
                            ways = (ways + dp[target[0]][target[1]]) % MOD
                            
                    dp[r][c] = ways
                    
        return dp[0][0]