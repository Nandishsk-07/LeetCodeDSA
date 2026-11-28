class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        freq = [0] * (n + 1)
        global_min_p = 10**18
        for f, p in items:
            freq[f] += 1
            if p < global_min_p:
                global_min_p = p
        mult_count = [0] * (n + 1)
        for f in xrange(1, n + 1):
            if freq[f] > 0:
                total = 0
                for m in xrange(f, n + 1, f):
                    total += freq[m]
                mult_count[f] = total
        bundles = []
        for f, p in items:
            cap = mult_count[f] - 1
            if cap > 0:
                bundles.append((p, cap))
        bundles.sort()
        ans = budget // global_min_p
        curr_cost = 0
        curr_items = 0
        for price, cap in bundles:
            if curr_cost >= budget:
                break
            rem_budget = budget - curr_cost
            max_take = min(cap, rem_budget // price)
            leftover = rem_budget - max_take * price
            cand1 = curr_items + max_take * 2 + (leftover // global_min_p)
            if cand1 > ans:
                ans = cand1
            if max_take > 0:
                leftover2 = leftover + price
                cand2 = curr_items + (max_take - 1) * 2 + (leftover2 // global_min_p)
                if cand2 > ans:
                    ans = cand2
            if max_take < cap:
                break
            curr_cost += cap * price
            curr_items += cap * 2
        return ans
        