class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        adj = [[] for _ in xrange(n)]
        for i in xrange(1, n):
            adj[parent[i]].append(i)
        new_parent = list(parent)
        last_seen = [[] for _ in xrange(26)]
        stack = [(0, 0)]
        while stack:
            u, state = stack.pop()
            c = ord(s[u]) - ord('a')
            if state == 0:
                if last_seen[c]:
                    new_parent[u] = last_seen[c][-1]
                last_seen[c].append(u)
                stack.append((u, 1))
                for v in adj[u]:
                    stack.append((v, 0))
            else:
                last_seen[c].pop()        
        new_adj = [[] for _ in xrange(n)]
        for i in xrange(1, n):
            new_adj[new_parent[i]].append(i)    
        order = []
        dfs_stack = [0]
        while dfs_stack:
            u = dfs_stack.pop()
            order.append(u)
            for v in new_adj[u]:
                dfs_stack.append(v)
        ans = [1] * n
        for u in reversed(order):
            p = new_parent[u]
            if p != -1:
                ans[p] += ans[u]
        return ans
        