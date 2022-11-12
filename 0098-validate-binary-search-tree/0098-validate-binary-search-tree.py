# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = list()
        inorder = list()
        
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if inorder and root.val <= inorder[-1]: return False
            inorder.append(root.val)
            root = root.right
        
        return True