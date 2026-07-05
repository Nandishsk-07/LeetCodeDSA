class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        MOD = 10**9 + 7
        dp = [[[0, 0] for _ in xrange(n)] for _ in xrange(n)]
        dp[n-1][n-1] = [0, 1]
        for r in xrange(n - 1, -1, -1):
            for c in xrange(n - 1, -1, -1):
                if r == n - 1 and c == n - 1:
                    continue
                if board[r][c] == 'X':
                    continue
                max_s, paths = -1, 0
                directions = [(r + 1, c), (r, c + 1), (r + 1, c + 1)]
                for nr, nc in directions:
                    if nr < n and nc < n and dp[nr][nc][1] > 0:
                        prev_score, prev_paths = dp[nr][nc]
                        if prev_score > max_s:
                            max_s = prev_score
                            paths = prev_paths
                        elif prev_score == max_s:
                            paths = (paths + prev_paths) % MOD
                if max_s != -1:
                    current_value = 0 if board[r][c] == 'E' else int(board[r][c])
                    dp[r][c] = [max_s + current_value, paths]
        return dp[0][0] if dp[0][0][1] > 0 else [0, 0]
        