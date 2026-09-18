class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        valid_intervals = []
        for ch in first:
            l = first[ch]
            r = last[ch]
            is_valid = True
            k = l
            while k <= r:
                char_k = s[k]
                if first[char_k] < l:
                    is_valid = False
                    break
                r = max(r, last[char_k])
                k += 1
            if is_valid:
                valid_intervals.append((r, l))
        valid_intervals.sort()
        res = []
        prev_end = -1
        for r, l in valid_intervals:
            if l > prev_end:
                res.append(s[l:r + 1])
                prev_end = r
        return res
        