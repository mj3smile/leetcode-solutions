# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if not root or not root.left:
            return root
        
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        level = 1
        while queue:
            values = []
            if level % 2 != 0:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    values.append(node.val)
                    queue.append(node)

            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 != 0:
                    node.val = values.pop()
                if not node.left:
                    continue
                queue.append(node.left)
                queue.append(node.right)
            level += 1
        
        return root