# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.preorder = preorder
        self.inorder_indexes = dict()
        self.preorder_indexes = dict()
        for i in range(len(preorder)):
            p_val, i_val = preorder[i], inorder[i]
            self.inorder_indexes[i_val] = i
            self.preorder_indexes[p_val] = i
        
        return self.construct(0, len(preorder) - 1, 0, len(inorder) - 1)

    def construct(self, p_start, p_end, i_start, i_end):
        if p_start < 0 or p_start == len(self.preorder) or p_end < 0 or p_end == len(self.preorder) or p_start > p_end:
            return None
        
        if i_start < 0 or i_start == len(self.inorder) or i_end < 0 or i_end == len(self.inorder) or i_start > i_end:
            return None

        print(f"p_start: {p_start}, p_end: {p_end}, i_start: {i_start}, i_end: {i_end}")
        root_val = self.preorder[p_start]
        root = TreeNode(root_val)

        right_p_start, right_p_end = p_start + 1, p_end
        left_p_start, left_p_end = p_start + 1, p_end

        inorder_index = self.inorder_indexes[root_val]
        if inorder_index > i_start:
            left_p_end = p_start + inorder_index - i_start
            right_p_start = left_p_end + 1
        else:
            left_p_start = right_p_end + 1

        
        root.left = self.construct(left_p_start, left_p_end, i_start, inorder_index-1)
        root.right = self.construct(right_p_start, right_p_end, inorder_index+1, i_end)
        return root