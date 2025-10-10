# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.result = 0
        # left = self.countMaxDepth(root.left)
        # right = self.countMaxDepth(root.right)

        # print(f"left: {left}, right: {right}")
        self.countMaxDepth(root)
        return self.result
    
    def countMaxDepth(self, root):
        if not root:
            return 0

        left = self.countMaxDepth(root.left)
        right = self.countMaxDepth(root.right)

        self.result = max(self.result, left + right)        
        return 1 + max(self.countMaxDepth(root.left), self.countMaxDepth(root.right))