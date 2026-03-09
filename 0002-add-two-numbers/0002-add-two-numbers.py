# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr = result
        remainder = 0

        while l1 or l2 or remainder > 0:
            total = 0 + remainder
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            if total > 9:
                remainder = 1
                total = total % 10
            else:
                remainder = 0

            curr.next = ListNode(total)
            curr = curr.next
        
        return result.next