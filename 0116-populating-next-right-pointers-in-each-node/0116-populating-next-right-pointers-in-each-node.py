"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            next_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                node.next = next_node
                next_node = node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return root