class SegmentTree:
    def __init__(self, n: int, MOD: int):
        self.n = n
        self.MOD = MOD
        self.sum_val = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
    def _apply(self, node: int, l: int, r: int, val: int):
        MOD = self.MOD
        length = r - l + 1
        val %= MOD
        self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.sum_val[node] + val * val % MOD * length) % MOD
        self.sum_val[node] = (self.sum_val[node] + val * length) % MOD
        self.lazy[node] = (self.lazy[node] + val) % MOD
    def _push(self, node: int, l: int, r: int):
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            left = 2 * node
            right = 2 * node + 1
            self._apply(left, l, mid, self.lazy[node])
            self._apply(right, mid + 1, r, self.lazy[node])
            self.lazy[node] = 0
    def update(self, node: int, l: int, r: int, ql: int, qr: int, val: int):
        if ql <= l and r <= qr:
            self._apply(node, l, r, val)
            return
        self._push(node, l, r)
        mid = (l + r) // 2
        left = 2 * node
        right = 2 * node + 1
        if ql <= mid:
            self.update(left, l, mid, ql, qr, val)
        if qr > mid:
            self.update(right, mid + 1, r, ql, qr, val)
        self.sum_val[node] = (self.sum_val[left] + self.sum_val[right]) % self.MOD
        self.sum_sq[node] = (self.sum_sq[left] + self.sum_sq[right]) % self.MOD
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        tree = SegmentTree(n, MOD)
        last_pos = {}
        total_ans = 0
        for i, x in enumerate(nums):
            prev = last_pos.get(x, -1)
            tree.update(1, 0, n - 1, prev + 1, i, 1)
            last_pos[x] = i
            total_ans = (total_ans + tree.sum_sq[1]) % MOD
        return total_ans
        