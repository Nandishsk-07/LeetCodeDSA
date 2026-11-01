class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0
        adj = [[] for _ in xrange(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        dist = [[float('inf')] * (k + 1) for _ in xrange(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        while pq:
            d, u, count = heapq.heappop(pq)
            if d > dist[u][count]:
                continue
            if u == n - 1:
                return d    
            u_label = labels[u]
            for v, w in adj[u]:
                if labels[v] == u_label:
                    next_count = count + 1
                    if next_count <= k:
                        if d + w < dist[v][next_count]:
                            dist[v][next_count] = d + w
                            heapq.heappush(pq, (d + w, v, next_count))
                else:
                    next_count = 1
                    if d + w < dist[v][next_count]:
                        dist[v][next_count] = d + w
                        heapq.heappush(pq, (d + w, v, next_count))       
        return -1
        