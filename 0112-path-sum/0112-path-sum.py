# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        
        if self.hasPathSum(root.left, targetSum):
            return True
        
        if self.hasPathSum(root.right, targetSum):
            return True
        
        return False
        
#         def calculate(root, total, targetSum):
#             if total == targetSum:
#                 return True
            
#             if not root or total > targetSum:
#                 return False
            
#             if calculate(root.left, total + root.val, targetSum):
#                 return True
#             if calculate(root.right, total + root.val, targetSum):
#                 return True
            
#             return False
        
#         return calculate(root, 0, targetSum)