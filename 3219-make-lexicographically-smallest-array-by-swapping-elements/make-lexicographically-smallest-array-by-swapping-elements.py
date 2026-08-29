class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        sorted_pairs = sorted((nums[idx], idx) for idx in xrange(n))
        res = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                j += 1 
            group_values = [sorted_pairs[k][0] for k in xrange(i, j)]
            group_indices = sorted(sorted_pairs[k][1] for k in xrange(i, j))
            for k in xrange(len(group_values)):
                res[group_indices[k]] = group_values[k]
            i = j
        return res
        