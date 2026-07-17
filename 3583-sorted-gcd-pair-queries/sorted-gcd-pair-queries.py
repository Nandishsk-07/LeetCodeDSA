import bisect
from typing import List
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
        cnt = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                cnt[i] += freq[j]
        gcd_pair_counts = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            total_pairs = cnt[i] * (cnt[i] - 1) // 2
            for j in range(2 * i, max_val + 1, i):
                total_pairs -= gcd_pair_counts[j]         
            gcd_pair_counts[i] = total_pairs
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_pair_counts[i]
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)       
        return ans
        