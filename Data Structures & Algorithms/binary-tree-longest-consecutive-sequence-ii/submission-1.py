# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        visited = dict()
        def countConsecutive(node, prev):
            if not node or (prev - 1 != node.val and prev + 1 != node.val):
                return 0
            
            if node in visited:
                return visited[node]
            
            left = countConsecutive(node.left, node.val)
            right = countConsecutive(node.right, node.val)

            result = 1
            if node.left and node.right and (node.left.val < node.val < node.right.val or node.left.val > node.val > node.right.val):
                result += + left + right
            else:
                result += max(left, right)
            
            visited[node] = result
            return result
        
        result = 1
        def dfs(node):
            if not node:
                return
            nonlocal result
            result = max(result, countConsecutive(node, node.val - 1))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result
        
