# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def dfs(node, maxPrevValue):
            if not node:
                return
            if maxPrevValue <= node.val:
                nonlocal result
                result += 1
            dfs(node.left, max(maxPrevValue, node.val))
            dfs(node.right, max(maxPrevValue, node.val))
        dfs(root, root.val)
        return result