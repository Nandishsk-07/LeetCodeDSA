class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ""   
        n = len(s)
        ans = ""
        ones_count = 0
        left = 0
        for right in range(n):
            if s[right] == '1':
                ones_count += 1
            while ones_count == k:
                if s[left] == '1':
                    curr = s[left:right + 1]
                    if not ans or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                        ans = curr
                    ones_count -= 1
                left += 1
        return ans
        