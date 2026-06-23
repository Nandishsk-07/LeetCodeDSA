class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        num_vals = r - l + 1
        if num_vals <= 1:
            return 0
        dp_0 = [(num_vals - 1 -v) % MOD for v in range(num_vals)]
        dp_1 = [v % MOD for v in range(num_vals)]
        for _ in range(3, n + 1):
            pref_down = [0] * (num_vals + 1)
            pref_up = [0] * (num_vals + 1)
            for v in range(num_vals):
                pref_down[v + 1] = (pref_down[v] + dp_0[v]) % MOD
                pref_up[v + 1] = (pref_up[v] + dp_1[v]) % MOD
            total_up = pref_up[num_vals]
            dp_0 = [(total_up - p) % MOD for p in pref_up[1:]]
            dp_1 = pref_down[:num_vals]
        return (sum(dp_0) + sum(dp_1)) % MOD
   