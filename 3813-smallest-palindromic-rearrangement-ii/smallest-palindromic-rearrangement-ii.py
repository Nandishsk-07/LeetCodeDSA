import collections
class Solution(object):
    def __init__(self):
        self.MAX = 10**6 + 1
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = collections.Counter(s)   
        odd_count = sum(1 for freq in count.values() if freq % 2 == 1)
        if odd_count > 1:
            return ""       
        half_count = [0] * 26
        mid_letter = ""
        for char, freq in count.items():
            half_count[ord(char) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid_letter = char           
        total_perm = self._count_arrangements(half_count)
        if k > total_perm:
            return ""        
        left_half = self._generate_left_half(half_count, k)   
        return "".join(left_half) + mid_letter + "".join(reversed(left_half))
    def _generate_left_half(self, half_count, k):
        half_len = sum(half_count)
        left = []
        for _ in xrange(half_len):
            for i, freq in enumerate(half_count):
                if freq == 0:
                    continue       
                half_count[i] -= 1
                arrangements = self._count_arrangements(half_count)   
                if arrangements >= k:
                    left.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    half_count[i] += 1 
        return left
    def _count_arrangements(self, count):
        total = sum(count)
        res = 1
        for freq in count:
            res *= self._nCk(total, freq)
            if res >= self.MAX:
                return self.MAX
            total -= freq
        return res
    def _nCk(self, n, k):
        res = 1
        for i in xrange(1, min(k, n - k) + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX:
                return self.MAX
        return res
        