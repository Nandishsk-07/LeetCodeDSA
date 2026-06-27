from collections import Counter
from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_len = 1
        if 1 in counts:
            c = counts[1]
            if c % 2 == 0:
                max_len = max(max_len, c - 1)
            else:
                max_len = max(max_len, c)
        for x in list(counts.keys()):
            if x == 1:
                continue               
            current_len = 0
            current_base = x
            while counts[current_base] >= 2:
                current_len += 2
                current_base = current_base * current_base
            if counts[current_base] == 1:
                current_len += 1
            else:
                current_len -= 1                
            max_len = max(max_len, current_len)           
        return max_len
        