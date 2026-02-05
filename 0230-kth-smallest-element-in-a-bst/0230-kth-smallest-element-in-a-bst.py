# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0
        heap = list()
        heapq.heapify(heap)

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            heapq.heappush(heap, -node.val)
            if len(heap) > k:
                heapq.heappop(heap)

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return heapq.heappop(heap) * -1