# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        if self.isIdentical(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def isIdentical(self, root, subRoot):
        if not subRoot and not root:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.isIdentical(root.left, subRoot.left) and self.isIdentical(root.right, subRoot.right)
        
        return False
            
        