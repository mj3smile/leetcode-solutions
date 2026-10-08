# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new = None
        def dfs(r):
            if not r:
                return
            if not r.left:
                nonlocal new
                new = r
                return
            
            dfs(r.left)
            left = r.left
            right = r.right

            r.left.left = r.right
            r.left.right = r
            r.left, r.right = None, None
        
        dfs(root)
        return new