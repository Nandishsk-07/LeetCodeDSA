class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        m = len(s)
        MOD = 10**9 + 7       
        pow10 = [1] * (m + 1)
        for i in xrange(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD           
        pref_nonzero_cnt = [0] * (m + 1)
        pref_digit_sum = [0] * (m + 1)
        pref_x = [0] * (m + 1)        
        for i in xrange(m):
            digit = int(s[i])
            if digit != 0:
                pref_nonzero_cnt[i + 1] = pref_nonzero_cnt[i] + 1
                pref_digit_sum[i + 1] = pref_digit_sum[i] + digit
                pref_x[i + 1] = (pref_x[i] * 10 + digit) % MOD
            else:
                pref_nonzero_cnt[i + 1] = pref_nonzero_cnt[i]
                pref_digit_sum[i + 1] = pref_digit_sum[i]
                pref_x[i + 1] = pref_x[i]                
        ans = []
        for L, R in queries:
            digit_sum = pref_digit_sum[R + 1] - pref_digit_sum[L]
            num_nonzero = pref_nonzero_cnt[R + 1] - pref_nonzero_cnt[L]           
            if num_nonzero == 0:
                ans.append(0)
                continue              
            x = (pref_x[R + 1] - pref_x[L] * pow10[num_nonzero]) % MOD
            score = (x * digit_sum) % MOD
            ans.append(score)           
        return ans
        