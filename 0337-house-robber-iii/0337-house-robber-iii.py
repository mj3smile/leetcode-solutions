# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = dict()
        def dfs(root):
            if not root:
                return 0
            if root in cache:
                return cache[root]
        
            rob_curr = root.val
            if root.left:
                rob_curr += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                rob_curr += dfs(root.right.left) + dfs(root.right.right)
            
            rob_child = dfs(root.left)
            rob_child += dfs(root.right)
            cache[root] = max(rob_curr, rob_child)
            return cache[root]
        
        return dfs(root)
        