class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = list(set(nums))
        n = len(unique_nums) 
        pair_xors = set()
        for i in xrange(n):
            for j in xrange(i, n):
                pair_xors.add(unique_nums[i] ^ unique_nums[j]) 
        triplet_xors = set()
        for pair_val in pair_xors:
            for num in unique_nums:
                triplet_xors.add(pair_val ^ num)        
        return len(triplet_xors)
        