# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(l, r, head):
            mid = (l + r) // 2
            head.val = nums[mid]
            
            if mid - 1 >= 0 and mid - 1 >= l:
                head.left = TreeNode()
                convert(l, mid - 1, head.left)
            if mid + 1 < len(nums) and mid + 1 <= r:
                head.right = TreeNode()
                convert(mid + 1, r, head.right)
        
        head = TreeNode()
        convert(0, len(nums) - 1, head)
        return head
            