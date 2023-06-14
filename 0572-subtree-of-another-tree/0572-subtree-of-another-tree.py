# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s = []
        def dfs(root):
            if not root:
                return
            
            if root.val == subRoot.val:
                s.append(root)
            
            dfs(root.left)
            dfs(root.right)
        
        def isIdentical(root, subRoot):
            if not subRoot and not root:
                return True
            
            if root and subRoot and root.val == subRoot.val:
                return isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)
            else:
                return False
                
        
        dfs(root)
        for sub in s:
            if isIdentical(sub, subRoot):
                return True
        
        return False
            
        