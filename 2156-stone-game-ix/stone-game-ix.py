class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        c = [0,0,0]
        for stone in stones:
            c[stone % 3] += 1
        c0, c1, c2 = c[0], c[1], c[2]
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        return abs(c1 - c2) > 2
        