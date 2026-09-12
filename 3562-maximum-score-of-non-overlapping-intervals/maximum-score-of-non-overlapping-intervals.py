class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted([(r, l, w, i) for i, (l, r, w) in enumerate(intervals)])
        r_ends = [x[0] for x in arr]
        def is_better(cand, curr):
            if cand[0] != curr[0]:
                return cand[0] > curr[0]
            return cand[1] < curr[1]
        dp_table = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            r, l, w, orig_idx = arr[i - 1]
            p = bisect_left(r_ends, l)
            for c in range(1, 5):
                best_state = dp_table[i - 1][c]
                prev_score, prev_indices = dp_table[p][c - 1]
                new_score = prev_score + w
                new_indices = sorted(prev_indices + [orig_idx])
                cand_state = (new_score, new_indices)
                if is_better(cand_state, best_state):
                    best_state = cand_state
                dp_table[i][c] = best_state
        ans = (0, [])
        for c in range(1, 5):
            if is_better(dp_table[n][c], ans):
                ans = dp_table[n][c]
        return ans[1]
        