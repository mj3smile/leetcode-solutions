# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = []
        
        def dfs(root):
            if not root or len(smallest) == k:
                return
            
            dfs(root.left)
            smallest.append(root.val)
            dfs(root.right)
        
        dfs(root)
        print(smallest)
        return smallest[k - 1]