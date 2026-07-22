import bisect
from typing import List

class SparseTable:
    def __init__(self, arr: List[int]):
        n = len(arr)
        if n == 0:
            self.st = []
            return
        self.LOG = n.bit_length()
        self.st = [[0] * n for _ in range(self.LOG)]
        self.st[0] = list(arr)
        
        for i in range(1, self.LOG):
            for j in range(n - (1 << i) + 1):
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])

    def query(self, L: int, R: int) -> int:
        if L > R or not self.st:
            return 0
        length = R - L + 1
        k = length.bit_length() - 1
        return max(self.st[k][L], self.st[k][R - (1 << k) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        # Build zero-group information
        zero_groups = []  # (start_idx, length)
        zero_group_index = [-1] * n
        
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    zero_group_index[i] = len(zero_groups)
                    i += 1
                zero_groups.append((start, i - start))
            else:
                i += 1
                
        m = len(zero_groups)
        
        # Precompute sum of adjacent zero-group lengths for RMQ
        adjacent_sums = []
        for j in range(m - 1):
            adjacent_sums.append(zero_groups[j][1] + zero_groups[j + 1][1])
            
        st = SparseTable(adjacent_sums)
        
        ans = []
        for l, r in queries:
            max_gain = 0
            
            # Map boundary indices l and r to zero-group indices
            start_g = zero_group_index[l]
            if start_g == -1:
                start_g = bisect.bisect_left(zero_groups, (l, -1))
                
            end_g = zero_group_index[r]
            if end_g == -1:
                end_g = bisect.bisect_right(zero_groups, (r + 1, -1)) - 1
                
            # Need at least two distinct zero groups in [l, r] to do a trade
            if start_g >= end_g or start_g < 0 or end_g >= m:
                ans.append(total_ones)
                continue
                
            # Clipped lengths of boundary zero groups inside [l, r]
            left_len = (zero_groups[start_g][0] + zero_groups[start_g][1]) - l
            right_len = r - zero_groups[end_g][0] + 1
            
            # Case 1: Exactly adjacent zero groups at l and r
            if s[l] == '0' and s[r] == '0' and zero_group_index[l] + 1 == zero_group_index[r]:
                max_gain = max(max_gain, left_len + right_len)
            else:
                # Case 2: Fully contained adjacent zero-group pairs in range
                adj_l = start_g + 1 if s[l] == '0' else start_g
                adj_r = end_g - 1 if s[r] == '0' else end_g
                
                if adj_l <= adj_r - 1:
                    max_gain = max(max_gain, st.query(adj_l, adj_r - 1))
                    
                # Case 3: Boundary zero group + next full zero group
                limit_r = end_g if s[r] == '1' else end_g - 1
                if s[l] == '0' and zero_group_index[l] + 1 <= limit_r:
                    next_full = zero_groups[zero_group_index[l] + 1][1]
                    max_gain = max(max_gain, left_len + next_full)
                    
                # Case 4: Boundary zero group + previous full zero group
                limit_l = start_g if s[l] == '1' else start_g + 1
                if s[r] == '0' and zero_group_index[r] - 1 >= limit_l:
                    prev_full = zero_groups[zero_group_index[r] - 1][1]
                    max_gain = max(max_gain, right_len + prev_full)
                    
            ans.append(total_ones + max_gain)
            
        return ans