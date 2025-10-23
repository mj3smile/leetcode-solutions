# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.val = []
        return self.checkValidBST(root)
    
    def checkValidBST(self, node):
        if not node:
            return True
        
        left = self.checkValidBST(node.left)
        center = True
        if self.val and self.val[0] >= node.val:
            center = False
        if self.val:
            self.val[0] = node.val
        else:
            self.val.append(node.val)
        right = self.checkValidBST(node.right)

        return left and center and right