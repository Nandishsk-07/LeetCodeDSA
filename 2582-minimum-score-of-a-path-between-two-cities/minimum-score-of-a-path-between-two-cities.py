class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in xrange(n + 1)]
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        min_score = float('inf')
        while q:
            u = q.popleft()
            for v, d in adj[u]:
                if d < min_score:
                    min_score = d
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return min_score
        