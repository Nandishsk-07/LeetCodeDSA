class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        good_pairs = 0
        for num in nums:
            count = counts.get(num, 0)
            good_pairs += count
            counts[num] = count + 1
        return good_pairs
        