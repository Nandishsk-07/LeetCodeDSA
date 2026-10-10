class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        insertions = 0
        needed_right = 0
        for ch in s:
            if ch == '(':
                if needed_right % 2 != 0:
                    insertions += 1
                    needed_right -= 1
                needed_right += 2
            else:
                needed_right -= 1
                if needed_right < 0:
                    insertions += 1
                    needed_right = 1
        return insertions + needed_right
        