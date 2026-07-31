from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_freqs = sorted(freq.values(), reverse=True)
        total_pushes = 0
        for i, count in enumerate(sorted_freqs):
            push_cost = (i // 8) + 1
            total_pushes += count * push_cost
        return total_pushes
        