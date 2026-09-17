# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        orphan = set()
        for d in descriptions:
            orphan.add(d[0])

        for d in descriptions:
            parent, child, isLeft = d
            nodes[parent] = nodes.get(parent, TreeNode(val=parent))
            nodes[child] = nodes.get(child, TreeNode(val=child))
            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            if child in orphan:
                orphan.remove(child)
        
        root = 0
        for i in orphan:
            root = i
            break
        
        return nodes[root]