class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        opt1 = need1 * cost1 + need2 * cost2
        shared = min(need1, need2)
        rem1 = need1 - shared
        rem2 = need2 - shared
        opt2 = shared * costBoth + rem1 * cost1 + rem2 * cost2
        opt3 = max(need1, need2) * costBoth
        return min(opt1, opt2, opt3)
        