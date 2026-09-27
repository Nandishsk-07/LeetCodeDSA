class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        pair = [0] * n
        stack = []
        for i in xrange(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i        
        res = []
        i = 0
        direction = 1
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction
        return "".join(res)
        