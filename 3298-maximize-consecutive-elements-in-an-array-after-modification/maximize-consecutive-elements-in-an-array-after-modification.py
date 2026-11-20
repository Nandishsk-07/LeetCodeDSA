class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = defaultdict(int)
        for x in nums:
            if dp[x] + 1 > dp[x + 1]:
                dp[x + 1] = dp[x] + 1
            if dp[x - 1] + 1 > dp[x]:
                dp[x] = dp[x - 1] + 1
        return max(dp.values())
        