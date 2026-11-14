class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        pref = [0] * (n + 1)
        for i in xrange(n):
            pref[i + 1] = pref[i] + nums[i]
        min_sum = float('inf')
        for i in xrange(n - l + 1):
            end_limit = min(n, i + r)
            for j in xrange(i + l, end_limit + 1):
                curr_sum = pref[j] - pref[i]
                if 0 < curr_sum < min_sum:
                    min_sum = curr_sum
        return min_sum if min_sum != float('inf') else -1
        