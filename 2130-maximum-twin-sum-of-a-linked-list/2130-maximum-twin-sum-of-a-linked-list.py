# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []
        result = 0
        
        while head:
            nodes.append(head.val)
            head = head.next
        
        for l in range(len(nodes) // 2):
            r = len(nodes) - 1 - l
            result = max(result, nodes[l] + nodes[r])
        
        return result