from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_sorted = sorted(list(set(arr)))
        rank_map = {}
        for rank, val in enumerate(unique_sorted, 1):
            rank_map[val] = rank
        return [rank_map[x] for x in arr]
        