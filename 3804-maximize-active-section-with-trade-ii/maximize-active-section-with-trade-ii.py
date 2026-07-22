import bisect

class SparseTable(object):
    def __init__(self, arr):
        n = len(arr)
        if n == 0:
            self.st = []
            return
        self.LOG = 0
        while (1 << self.LOG) <= n:
            self.LOG += 1
            
        self.st = [[0] * n for _ in xrange(self.LOG)]
        self.st[0] = list(arr)
        
        for i in xrange(1, self.LOG):
            for j in xrange(n - (1 << i) + 1):
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])

    def query(self, L, R):
        if L > R or not self.st:
            return 0
        length = R - L + 1
        k = 0
        while (1 << (k + 1)) <= length:
            k += 1
        return max(self.st[k][L], self.st[k][R - (1 << k) + 1])


class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        total_ones = s.count('1')
        
        zero_groups = []
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
        
        adjacent_sums = []
        for j in xrange(m - 1):
            adjacent_sums.append(zero_groups[j][1] + zero_groups[j + 1][1])
            
        st = SparseTable(adjacent_sums)
        
        ans = []
        for l, r in queries:
            max_gain = 0
            
            start_g = zero_group_index[l]
            if start_g == -1:
                start_g = bisect.bisect_left(zero_groups, (l, -1))
                
            end_g = zero_group_index[r]
            if end_g == -1:
                end_g = bisect.bisect_right(zero_groups, (r + 1, -1)) - 1
                
            if start_g >= end_g or start_g < 0 or end_g >= m:
                ans.append(total_ones)
                continue
                
            left_len = (zero_groups[start_g][0] + zero_groups[start_g][1]) - l
            right_len = r - zero_groups[end_g][0] + 1
            
            if s[l] == '0' and s[r] == '0' and zero_group_index[l] + 1 == zero_group_index[r]:
                max_gain = max(max_gain, left_len + right_len)
            else:
                adj_l = start_g + 1 if s[l] == '0' else start_g
                adj_r = end_g - 1 if s[r] == '0' else end_g
                
                if adj_l <= adj_r - 1:
                    max_gain = max(max_gain, st.query(adj_l, adj_r - 1))
                    
                limit_r = end_g if s[r] == '1' else end_g - 1
                if s[l] == '0' and zero_group_index[l] + 1 <= limit_r:
                    next_full = zero_groups[zero_group_index[l] + 1][1]
                    max_gain = max(max_gain, left_len + next_full)
                    
                limit_l = start_g if s[l] == '1' else start_g + 1
                if s[r] == '0' and zero_group_index[r] - 1 >= limit_l:
                    prev_full = zero_groups[zero_group_index[r] - 1][1]
                    max_gain = max(max_gain, right_len + prev_full)
                    
            ans.append(total_ones + max_gain)
            
        return ans
        