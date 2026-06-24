class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        V = r - l + 1       
        if V <= 1:
            return 0            
        def multiply(A, B):
            cols = [list(x) for x in zip(*B)]
            return [
                [sum(x * y for x, y in zip(row, col)) % MOD for col in cols]
                for row in A
            ]
        def power(A, p):
            res = [[0] * V for _ in range(V)]
            for i in range(V):
                res[i][i] = 1
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res
        base_down = [(V - 1 - v) % MOD for v in range(V)]
        base_up = [v % MOD for v in range(V)]       
        steps = n - 2
        k = steps // 2        
        P = [[(V - 1 - max(i, j)) % MOD for j in range(V)] for i in range(V)]
        Q = [[min(i, j) % MOD for j in range(V)] for i in range(V)]        
        Pk = power(P, k)
        Qk = power(Q, k)        
        if steps % 2 == 0:
            final_down = [sum(Pk[i][j] * base_down[j] for j in range(V)) % MOD for i in range(V)]
            final_up = [sum(Qk[i][j] * base_up[j] for j in range(V)) % MOD for i in range(V)]
        else:
            mid_down = [sum(base_up[j] for j in range(i + 1, V)) % MOD for i in range(V)]
            mid_up = [sum(base_down[j] for j in range(i)) % MOD for i in range(V)]           
            final_down = [sum(Pk[i][j] * mid_down[j] for j in range(V)) % MOD for i in range(V)]
            final_up = [sum(Qk[i][j] * mid_up[j] for j in range(V)) % MOD for i in range(V)]           
        return (sum(final_down) + sum(final_up)) % MOD
        