class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            groups = []
            for i in xrange(0, len(s), k):
                group_sum = sum(int(ch) for ch in s[i : i + k])
                groups.append(str(group_sum))
            s = "".join(groups)
        return s
        