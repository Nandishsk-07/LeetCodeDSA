from itertools import permutations
from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_numbers = set()
        for d1, d2, d3 in permutations(digits, 3):
            if d1 != 0 and d3 % 2 == 0:
                num = d1 * 100 + d2 * 10 + d3
                unique_numbers.add(num)
        return len(unique_numbers)
        