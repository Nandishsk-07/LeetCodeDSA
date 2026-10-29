import sys
sys.setrecursionlimit(200000)
class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 2)
    def update(self, idx: int, delta: int):
        while idx <= self.size:
            self.tree[idx] ^= delta
            idx += idx & -idx
    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res ^= self.tree[idx]
            idx -= idx & -idx
        return res
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG = 17
        up = [[0] * LOG for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        timer = 0
        stack = [(0, -1, 0, 0)]  
        while stack:
            u, p, d, state = stack.pop()
            if state == 0:
                timer += 1
                tin[u] = timer
                depth[u] = d
                up[u][0] = p if p != -1 else 0
                for k in range(1, LOG):
                    up[u][k] = up[up[u][k - 1]][k - 1]
                stack.append((u, p, d, 1))
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, d + 1, 0))
            else:
                tout[u] = timer
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = up[u][k]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[u][k] != up[v][k]:
                    u = up[u][k]
                    v = up[v][k]
            return up[u][0]
        bit = FenwickTree(timer)
        node_char = list(s)
        for i in range(n):
            mask = 1 << (ord(node_char[i]) - ord('a'))
            bit.update(tin[i], mask)
            bit.update(tout[i] + 1, mask)
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                if node_char[u] != c:
                    old_mask = 1 << (ord(node_char[u]) - ord('a'))
                    new_mask = 1 << (ord(c) - ord('a'))
                    diff = old_mask ^ new_mask
                    bit.update(tin[u], diff)
                    bit.update(tout[u] + 1, diff)
                    node_char[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                mask_u = bit.query(tin[u])
                mask_v = bit.query(tin[v])
                mask_lca = bit.query(tin[lca])
                lca_char_mask = 1 << (ord(node_char[lca]) - ord('a'))
                path_mask = mask_u ^ mask_v ^ mask_lca ^ (mask_lca ^ lca_char_mask)
                ans.append(path_mask == 0 or (path_mask & (path_mask - 1)) == 0)
        return ans
        