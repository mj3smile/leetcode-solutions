# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sums_head = ListNode()
        curr = sums_head
        
        left = 0
        while l1 or l2 or left > 0:
            n1 = 0 if not l1 else l1.val
            n2 = 0 if not l2 else l2.val
            add = left + n1 + n2
            left = add // 10
            node = ListNode(val=add%10)
            curr.next = node
            curr = curr.next
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        return sums_head.next
