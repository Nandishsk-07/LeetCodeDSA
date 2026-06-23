class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1
        return count
        