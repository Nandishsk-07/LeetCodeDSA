class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()
        for i, char in enumerate(s):
            if char in seen:
                continue
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return "".join(stack)