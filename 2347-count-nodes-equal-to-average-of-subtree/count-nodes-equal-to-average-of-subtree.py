# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        def dfs(node):
            if not node:
                return 0, 0
            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)
            curr_sum = left_sum + right_sum + node.val
            curr_nodes = left_nodes + right_nodes + 1
            if curr_sum // curr_nodes == node.val:
                self.count += 1
            return curr_sum, curr_nodes
        dfs(root)
        return self.count
        