# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        result = list()
        
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == 0: result.append(curr.val)
                
                if curr.right:
                    queue.append(curr.right)
                
                if curr.left:
                    queue.append(curr.left)
        
        return result