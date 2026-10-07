class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        queue = set([s])
        while queue:
            valid = [string for string in queue if is_valid(string)]
            if valid:
                return valid
            next_level = set()
            for string in queue:
                for i in xrange(len(string)):
                    if string[i] in '()':
                        if i > 0 and string[i] == string[i - 1]:
                            continue
                        next_level.add(string[:i] + string[i + 1:])
            queue = next_level
        return [""]