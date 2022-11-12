# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = list()
        
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            level_val = list()
            for _ in range(len(queue)):
                curr = queue.popleft()
                level_val.append(curr.val)
                
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            result.append(level_val)
        
        return result