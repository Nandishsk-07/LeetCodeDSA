from collections import deque
from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1           
        visited = [False] * n
        complete_components_count = 0
        for i in range(n):
            if not visited[i]:
                q = deque([i])
                visited[i] = True               
                vertex_count = 0
                total_degree_sum = 0               
                while q:
                    u = q.popleft()
                    vertex_count += 1
                    total_degree_sum += degree[u]               
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                if total_degree_sum == vertex_count * (vertex_count - 1):
                    complete_components_count += 1                
        return complete_components_count
        