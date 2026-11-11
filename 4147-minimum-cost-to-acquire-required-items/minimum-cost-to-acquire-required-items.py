class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        opt1 = need1 * cost1 + need2 * cost2
        shared = min(need1, need2)
        rem1 = need1 - shared
        rem2 = need2 - shared
        opt2 = shared * costBoth + rem1 * cost1 + rem2 * cost2
        opt3 = max(need1, need2) * costBoth
        return min(opt1, opt2, opt3)
        