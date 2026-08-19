class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_count = defaultdict(int)
        for i in range(n - k + 1):
            unique_elements = set(nums[i:i + k])
            for val in unique_elements:
                subarray_count[val] += 1
        ans = -1
        for val, count in subarray_count.items():
            if count == 1:
                ans = max(ans, val)
        return ans