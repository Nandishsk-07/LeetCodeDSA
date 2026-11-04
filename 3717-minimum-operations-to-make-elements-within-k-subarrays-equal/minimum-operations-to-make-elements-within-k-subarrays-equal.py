from typing import List
import bisect
class Fenwick:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)
    def add(self, idx: int, delta: int):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx
    def query(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & -idx
        return s
    def find_kth(self, k: int) -> int:
        """Find smallest index with prefix count >= k via binary lifting."""
        idx = 0
        bit_mask = 1 << (self.size.bit_length() - 1)
        while bit_mask > 0:
            next_idx = idx + bit_mask
            if next_idx <= self.size and self.tree[next_idx] < k:
                idx = next_idx
                k -= self.tree[idx]
            bit_mask >>= 1
        return idx + 1
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        unique_vals = sorted(set(nums))
        U = len(unique_vals)
        val_to_rank = {v: i + 1 for i, v in enumerate(unique_vals)}
        bit_cnt = Fenwick(U)
        bit_sum = Fenwick(U)
        def add_val(val: int):
            r = val_to_rank[val]
            bit_cnt.add(r, 1)
            bit_sum.add(r, val)
        def remove_val(val: int):
            r = val_to_rank[val]
            bit_cnt.add(r, -1)
            bit_sum.add(r, -val)
        def get_cost() -> int:
            target_k = (x + 1) // 2
            med_rank = bit_cnt.find_kth(target_k)
            med_val = unique_vals[med_rank - 1]
            cnt_left = bit_cnt.query(med_rank)
            sum_left = bit_sum.query(med_rank)
            cnt_right = x - cnt_left
            sum_right = bit_sum.query(U) - sum_left
            return (cnt_left * med_val - sum_left) + (sum_right - cnt_right * med_val)
        costs = [0] * (n + 1)
        for i in range(x):
            add_val(nums[i])
        costs[x] = get_cost()
        for i in range(x, n):
            add_val(nums[i])
            remove_val(nums[i - x])
            costs[i + 1] = get_cost()
        INF = float('inf')
        prev_dp = [0] * (n + 1)
        for j in range(1, k + 1):
            curr_dp = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                curr_dp[i] = curr_dp[i - 1]
                take = prev_dp[i - x] + costs[i]
                if take < curr_dp[i]:
                    curr_dp[i] = take
            prev_dp = curr_dp
        return prev_dp[n]