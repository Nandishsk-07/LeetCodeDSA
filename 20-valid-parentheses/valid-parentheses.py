class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        matching = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in matching:
                if not stack or stack[-1] != matching[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0

        