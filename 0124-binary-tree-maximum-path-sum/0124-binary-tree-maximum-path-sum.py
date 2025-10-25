# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = -1000
        self.calculateMaxPath(root)
        return self.result
    
    def calculateMaxPath(self, root):
        if not root:
            return 0

        # self.result = max(self.result, root.val)
        left = self.calculateMaxPath(root.left)
        right = self.calculateMaxPath(root.right)
        self.result = max(self.result, root.val, root.val + left + right, root.val + left, root.val + right)
        
        root.val = max(root.val, root.val + max(left, right))
        return root.val