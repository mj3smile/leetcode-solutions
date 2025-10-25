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

        # if root.left or root.right:
        self.result = max(self.result, root.val)

        left = self.calculateMaxPath(root.left)
        right = self.calculateMaxPath(root.right)
        self.result = max(self.result, root.val + left + right, root.val + left, root.val + right)

        # if self.result:
        #     self.result[0] = max(self.result[0], root.val + left + right, root.val, left, right)
        # else:
        #     self.result.append(max(root.val + left + right, root.val, left, right))
        
        # if left and right:
        #     root.val = max(root.val, left.val, right.val, root.val + left.val + right.val, root.val + left.val, root.val + right.val)
        # elif left:
        #     root.val = max(root.val, left.val, root.val + left.val)
        # elif right:
        #     root.val = max(root.val, right.val, root.val + right.val)
        
        root.val = max(root.val, root.val + max(left, right))
        # self.result = max(self.result, root.val)
        # else:
        #     self.result = max(self.result, root.val)
        return root.val