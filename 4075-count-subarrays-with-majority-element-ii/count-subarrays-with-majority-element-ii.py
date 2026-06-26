class FenwickTree(object):
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size
    def update(self, i, delta):
        idx = i + 1
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)
    def query(self, i):
        idx = i + 1
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)
        return total
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        current_sum = 0
        for i in xrange(n):
            current_sum += 1 if nums[i] == target else -1
            prefix_sums[i + 1] = current_sum
        unique_vals = sorted(list(set(prefix_sums)))
        rank_map = {val: i for i, val in enumerate(unique_vals)}
        bit = FenwickTree(len(unique_vals))
        total_subarrays = 0
        for p_sum in prefix_sums:
            rank = rank_map[p_sum]
            if rank > 0:
                total_subarrays += bit.query(rank - 1)
            bit.update(rank, 1)
        return total_subarrays
        