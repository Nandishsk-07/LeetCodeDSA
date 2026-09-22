class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_cnt = [[0] * k for _ in range(4 * n)]
        def merge(left_prod, left_cnt, right_prod, right_cnt):
            prod = (left_prod * right_prod) % k
            cnt = list(left_cnt)
            for r in range(k):
                if right_cnt[r]:
                    new_rem = (left_prod * r) % k
                    cnt[new_rem] += right_cnt[r]
            return prod, cnt
        def build(node, l, r):
            if l == r:
                val_mod = nums[l] % k
                tree_prod[node] = val_mod
                tree_cnt[node] = [0] * k
                tree_cnt[node][val_mod] = 1
                return
            mid = (l + r) // 2
            left_child, right_child = 2 * node, 2 * node + 1
            build(left_child, l, mid)
            build(right_child, mid + 1, r)   
            tree_prod[node], tree_cnt[node] = merge(
                tree_prod[left_child], tree_cnt[left_child],
                tree_prod[right_child], tree_cnt[right_child]
            )
        def update(node, l, r, idx, val):
            if l == r:
                val_mod = val % k
                tree_prod[node] = val_mod
                tree_cnt[node] = [0] * k
                tree_cnt[node][val_mod] = 1
                return
            mid = (l + r) // 2
            left_child, right_child = 2 * node, 2 * node + 1
            if idx <= mid:
                update(left_child, l, mid, idx, val)
            else:
                update(right_child, mid + 1, r, idx, val)       
            tree_prod[node], tree_cnt[node] = merge(
                tree_prod[left_child], tree_cnt[left_child],
                tree_prod[right_child], tree_cnt[right_child]
            )
        def query_range(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_cnt[node]
            mid = (l + r) // 2
            left_child, right_child = 2 * node, 2 * node + 1    
            if qr <= mid:
                return query_range(left_child, l, mid, ql, qr)
            if ql > mid:
                return query_range(right_child, mid + 1, r, ql, qr)    
            lp, lc = query_range(left_child, l, mid, ql, qr)
            rp, rc = query_range(right_child, mid + 1, r, ql, qr)
            return merge(lp, lc, rp, rc)
        build(1, 0, n - 1)
        result = []
        for idx, val, start, x in queries:
            nums[idx] = val
            update(1, 0, n - 1, idx, val)
            _, cnt = query_range(1, 0, n - 1, start, n - 1)
            result.append(cnt[x])
        return result
        