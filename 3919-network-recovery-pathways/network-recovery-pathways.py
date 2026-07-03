class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        if not online[0] or not online[n - 1]:
            return -1
        valid_edges = []
        unique_costs = set()
        for u, v, cost in edges:
            if online[u] and online[v]:
                valid_edges.append((u, v, cost))
                unique_costs.add(cost)
        if not unique_costs:
            return -1
        sorted_costs = sorted(list(unique_costs))
        adj = [[] for _ in xrange(n)]
        in_degree = [0] * n
        for u, v, cost in valid_edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
        topo_order = []
        q = deque([i for i in xrange(n) if in_degree[i] == 0])
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        def check(threshold_cost):
            dp = [float('inf')] * n
            dp[0] = 0
            for u in topo_order:
                if dp[u] == float('inf'):
                    continue
                for v, cost in adj[u]:
                    if cost >= threshold_cost:
                        if dp[u] + cost < dp[v]:
                            dp[v] = dp[u] + cost
            return dp[n - 1] <= k
        left, right = 0, len(sorted_costs) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if check(sorted_costs[mid]):
                ans = sorted_costs[mid]
                left = mid + 1
            else:
                right = mid - 1
        return ans
        