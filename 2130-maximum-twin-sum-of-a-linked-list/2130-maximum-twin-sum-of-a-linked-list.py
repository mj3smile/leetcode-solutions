# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        
        # reverse the first half of the list
        # result: node1 <- node2 <- node3 -> node4 -> node5 -> node6
        # prev would be in node3 and slow would be in node 4 
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        result = 0
        while slow:
            result = max(result, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
            
        return result