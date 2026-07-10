from typing import List
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        LOG = 18 
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        orig_to_sorted = [0] * n
        for sorted_idx, (val, orig_idx) in enumerate(sorted_pairs):
            orig_to_sorted[orig_idx] = sorted_idx
        st = [[0] * LOG for _ in range(n)]
        
        r = 0
        for i in range(n):
            r = max(r, i)
            while r + 1 < n and sorted_pairs[r + 1][0] - sorted_pairs[i][0] <= maxDiff:
                r += 1
            st[i][0] = r
        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]
        ans = []
        for u, v in queries:
            a = orig_to_sorted[u]
            b = orig_to_sorted[v]
            if a > b:
                a, b = b, a
                
            if a == b:
                ans.append(0)
                continue              
            curr = a
            steps = 0
            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)
            if st[curr][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)           
        return ans
        