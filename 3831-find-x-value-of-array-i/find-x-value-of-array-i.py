class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            new_dp = [0] * k
            mod_val = num % k 
            new_dp[mod_val] += 1
            for r in xrange(k):
                if dp[r]:
                    new_rem = (r * mod_val) % k
                    new_dp[new_rem] += dp[r]
            for r in xrange(k):
                ans[r] += new_dp[r]
            dp = new_dp
        return ans
        