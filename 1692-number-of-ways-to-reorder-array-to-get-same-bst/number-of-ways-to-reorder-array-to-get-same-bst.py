class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 1000000007
        n = len(nums)
        comb = [[0] * (n + 1) for _ in xrange(n + 1)]
        for i in xrange(n + 1):
            comb[i][0] = 1
            for j in xrange(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
        def ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            c = comb[len(left) + len(right)][len(left)]
            return (c * ways(left) % MOD * ways(right)) % MOD
        return (ways(nums) - 1) % MOD
        