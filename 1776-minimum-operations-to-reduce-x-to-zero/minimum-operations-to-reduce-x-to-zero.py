class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total_sum = sum(nums)
        target = total_sum - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        max_len = -1
        current_sum = 0
        left = 0
        n = len(nums)
        for right in xrange(n):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        return n - max_len if max_len != -1 else -1
            
        
        