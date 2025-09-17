# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.items = list()
        self.convertToArr(root)

        for i in range(len(self.items) - 1):
            if self.items[i] >= self.items[i + 1]:
                return False
        
        return True
    
    def convertToArr(self, root):
        if root == None:
            return
        
        self.convertToArr(root.left)
        self.items.append(root.val)
        self.convertToArr(root.right)

    def validateSubtree(self, root, is_min_set, min_val, is_max_set, max_val):
        if root == None or (root.left == None and root.right == None):
            return True
        
        if root.left and (root.left.val >= root.val):
            return False
        
        if root.right and (root.right.val <= root.val):
            return False

        if is_min_set and root.left and root.left.val < min_val:
            return False
        
        if is_max_set and root.right and root.right.val > max_val:
            return False
        
        return True and self.validateSubtree(root.left, False, 0, True, root.val - 1) and self.validateSubtree(root.right, True, root.val + 1, False, 0)