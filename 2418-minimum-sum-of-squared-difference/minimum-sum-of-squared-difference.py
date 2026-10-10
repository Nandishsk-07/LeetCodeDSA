class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        max_diff = 0
        n = len(nums1)
        diffs = [0] * n
        total_diff = 0
        for i in xrange(n):
            d = abs(nums1[i] - nums2[i])
            diffs[i] = d
            total_diff += d
            if d > max_diff:
                max_diff = d
        if total_diff <= k:
            return 0
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
        for d in xrange(max_diff, 0, -1):
            if count[d] == 0:
                continue
            if k >= count[d]:
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                count[d] -= k
                count[d - 1] += k
                k = 0
                break
        ans = 0
        for d in xrange(1, max_diff + 1):
            if count[d]:
                ans += d * d * count[d]
        return ans
        