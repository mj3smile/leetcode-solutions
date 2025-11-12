"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes = dict()
        queue = deque()
        visited = set()
        if node:
            queue.append(node)
            visited.add(node.val)
        
        while queue:
            for _ in range(len(queue)):
                n = queue.popleft()
                nodes[n.val] = nodes.get(n.val, Node(n.val))
                
                for neighbor in n.neighbors:
                    nodes[neighbor.val] = nodes.get(neighbor.val, Node(neighbor.val))
                    nodes[n.val].neighbors.append(nodes[neighbor.val])
                    if neighbor.val in visited: continue
                    queue.append(neighbor)
                    visited.add(neighbor.val)
        
        return nodes.get(node.val, None) if node else None