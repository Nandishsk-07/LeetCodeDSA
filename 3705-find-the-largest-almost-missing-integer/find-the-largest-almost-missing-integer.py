class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        subarray_count = defaultdict(int)
        for i in xrange(n - k + 1):
            unique_elements = set(nums[i:i + k])
            for val in unique_elements:
                subarray_count[val] += 1       
        ans = -1
        for val, count in subarray_count.items():
            if count == 1:
                ans = max(ans, val)
        return ans
        