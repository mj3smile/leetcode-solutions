# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = 0
        self.findSmallest(root)
        return self.result

    def findSmallest(self, root):
        if not root:
            return
        
        self.findSmallest(root.left)
    
        if self.k == 0:
            return
        self.result = root.val
        self.k -= 1
        self.findSmallest(root.right)
