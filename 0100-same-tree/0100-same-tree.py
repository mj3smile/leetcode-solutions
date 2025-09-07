# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True

        node_identical = p.val == q.val if p != None and q != None else False
        child_identical = False
        if node_identical and p != None and q != None:
            child_identical = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return node_identical and child_identical