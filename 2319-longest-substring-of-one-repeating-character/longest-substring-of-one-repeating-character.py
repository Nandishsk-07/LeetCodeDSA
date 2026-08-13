class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s) 
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        tree_lc = [''] * (4 * n)
        tree_rc = [''] * (4 * n)
        def merge(node, l_child, r_child, l_len, r_len):
            tree_lc[node] = tree_lc[l_child]
            tree_rc[node] = tree_rc[r_child]  
            m = max(tree_max[l_child], tree_max[r_child])
            if tree_rc[l_child] == tree_lc[r_child]:
                m = max(m, tree_suff[l_child] + tree_pref[r_child])
                
                if tree_pref[l_child] == l_len:
                    tree_pref[node] = l_len + tree_pref[r_child]
                else:
                    tree_pref[node] = tree_pref[l_child]
                    
                if tree_suff[r_child] == r_len:
                    tree_suff[node] = r_len + tree_suff[l_child]
                else:
                    tree_suff[node] = tree_suff[r_child]
            else:
                tree_pref[node] = tree_pref[l_child]
                tree_suff[node] = tree_suff[r_child]        
            tree_max[node] = m
        def build(node, l, r):
            if l == r:
                tree_pref[node] = 1
                tree_suff[node] = 1
                tree_max[node] = 1
                tree_lc[node] = s[l]
                tree_rc[node] = s[l]
                return    
            mid = (l + r) // 2
            l_child = 2 * node
            r_child = 2 * node + 1    
            build(l_child, l, mid)
            build(r_child, mid + 1, r)    
            merge(node, l_child, r_child, mid - l + 1, r - mid)
        def update(node, l, r, idx, char):
            if l == r:
                tree_lc[node] = char
                tree_rc[node] = char
                return   
            mid = (l + r) // 2
            l_child = 2 * node
            r_child = 2 * node + 1   
            if idx <= mid:
                update(l_child, l, mid, idx, char)
            else:
                update(r_child, mid + 1, r, idx, char)        
            merge(node, l_child, r_child, mid - l + 1, r - mid)
        build(1, 0, n - 1)
        ans = []
        for i in xrange(len(queryCharacters)):
            ch = queryCharacters[i]
            idx = queryIndices[i]
            update(1, 0, n - 1, idx, ch)
            ans.append(tree_max[1])
        return ans
        