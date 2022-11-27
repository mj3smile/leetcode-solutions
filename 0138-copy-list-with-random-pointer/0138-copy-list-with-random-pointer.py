"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_copies = {None: None}
        
        i = head
        while i:
            nodes_copies[i] = Node(i.val)
            i = i.next
        
        i = head
        while i:
            copy = nodes_copies[i]
            copy.next = nodes_copies[i.next]
            copy.random = nodes_copies[i.random]
            i = i.next
            
        return nodes_copies[head]