# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        nodes = result

        remainder = 0
        while l1 or l2 or remainder > 0:
            first, second = 0, 0
            first_next, second_next = None, None
            if l1:
                first = l1.val
                first_next = l1.next
            if l2:
                second = l2.val
                second_next = l2.next

            total = first + second + remainder
            remainder = 0
            if total >= 10:
                remainder = total // 10
                total = total % 10

            nodes.next = ListNode(total)
            nodes = nodes.next
            l1 = first_next
            l2 = second_next
        
        return result.next