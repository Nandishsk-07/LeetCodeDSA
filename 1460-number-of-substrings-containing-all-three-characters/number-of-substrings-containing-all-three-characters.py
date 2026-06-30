class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_a, last_b, last_c = -1, -1, -1
        count = 0
        for i in xrange(len(s)):
            char = s[i]
            if char == 'a':
                last_a = i
            elif char == 'b':
                last_b = i
            else:
                last_c = i
            if last_a != -1 and last_b != -1 and last_c != -1:
                min_idx = last_a
                if last_b < min_idx: min_idx = last_b
                if last_c < min_idx: min_idx = last_c
                count += min_idx + 1
        return count
        