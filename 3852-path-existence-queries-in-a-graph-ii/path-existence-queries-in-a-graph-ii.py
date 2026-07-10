class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sorted_pairs = sorted((nums[i], i) for i in xrange(n))
        orig_to_sorted = [0] * n
        for sorted_idx, pair in enumerate(sorted_pairs):
            orig_to_sorted[pair[1]] = sorted_idx
        LOG = 18
        st = [[0] * LOG for _ in xrange(n)]
        r = 0
        for i in xrange(n):
            r = max(r, i)
            while r + 1 < n and sorted_pairs[r + 1][0] - sorted_pairs[i][0] <= maxDiff:
                r += 1
            st[i][0] = r
        for j in xrange(1, LOG):
            for i in xrange(n):
                st[i][j] = st[st[i][j - 1]][j - 1]
        ans = []
        for u, v in queries:
            a = orig_to_sorted[u]
            b = orig_to_sorted[v]
            if a > b:
                a, b = b, a
            if a == b:
                ans.append(0)
                continue
            curr = a
            steps = 0
            for j in xrange(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)
            if st[curr][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)
        return ans
        