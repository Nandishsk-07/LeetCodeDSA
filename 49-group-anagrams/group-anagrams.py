from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for string in strs:
            sorted_key = "".join(sorted(string))
            anagram_map[sorted_key].append(string)
            
        return list(anagram_map.values())