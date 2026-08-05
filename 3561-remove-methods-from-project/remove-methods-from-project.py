from collections import defaultdict, deque
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        adj = defaultdict(list)
        for u, v in invocations:
            adj[u].append(v) 
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
        return [i for i in range(n) if i not in suspicious]
        