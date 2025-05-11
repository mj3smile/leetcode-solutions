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
        old_nodes = list()
        val_to_index = dict() # key: val of old_nodes, val: arr of indexes which the val occur

        curr = head
        while curr:
            old_nodes.append(curr)
            val_to_index[curr.val] = val_to_index.get(curr.val, list())
            val_to_index[curr.val].append(len(old_nodes) - 1)
            curr = curr.next
        
        randoms = list() # randoms[i] is the index of random of old_nodes[i]
        for node in old_nodes:
            if not node.random:
                randoms.append(-1)
                continue

            for index in val_to_index[node.random.val]:
                if old_nodes[index] == node.random:
                    randoms.append(index)
                    break

        result = Node(0)
        curr = result
        new_nodes = [None] * len(old_nodes)
        for i in range(len(old_nodes)):
            old = old_nodes[i]
            random_index = randoms[i]

            new = Node(old.val)
            if new_nodes[i]:
                new = new_nodes[i]

            new_nodes[i] = new
            curr.next = new
            if random_index == -1:
                curr = curr.next
                continue

            new_random = Node(old_nodes[random_index].val)
            if new_nodes[random_index]:
                new_random = new_nodes[random_index]
            
            new_nodes[random_index] = new_random
            new.random = new_random
            curr = curr.next

        return result.next