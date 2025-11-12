"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_nodes = dict()
        neighbor_calculated = set()

        old_nodes = [node]
        while old_nodes:
            curr_node = old_nodes.pop()
            if curr_node == None or curr_node.val in neighbor_calculated:
                continue

            clone = cloned_nodes.get(curr_node.val, Node(curr_node.val))
            for n in curr_node.neighbors:
                neighbor_clone = cloned_nodes.get(n.val, Node(n.val))
                clone.neighbors.append(neighbor_clone)
                cloned_nodes[n.val] = neighbor_clone
                if n.val not in neighbor_calculated: old_nodes.append(n)

            cloned_nodes[curr_node.val] = clone
            neighbor_calculated.add(curr_node.val)
        
        return cloned_nodes[node.val]