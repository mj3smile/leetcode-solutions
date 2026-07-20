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
        clone = dict()
        random_waiting = dict()
        result = Node(-1)
        curr = result

        old = head
        while old:
            new = Node(old.val)
            curr.next = new
            curr = curr.next
            clone[old] = new

            if old in random_waiting:
                for i in range(len(random_waiting[old])):
                    random_waiting[old][i].random = new

            if not old.random:
                old = old.next
                continue
            
            if old.random in clone:
                new.random = clone[old.random]
            else:
                random_waiting[old.random] = random_waiting.get(old.random, list())
                random_waiting[old.random].append(new)
            
            old = old.next
        
        return result.next