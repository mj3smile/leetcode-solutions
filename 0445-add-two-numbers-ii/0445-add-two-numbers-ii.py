# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def convertToNum(head):
            num = 0
            while head:
                num = num * 10 + head.val
                head = head.next
            return num
        
        add = convertToNum(l1) + convertToNum(l2)
        if add == 0:
            return ListNode(val=0)

        prev = None
        while add > 0:
            last_digit = add % 10
            new_node = ListNode(val=last_digit)
            new_node.next = prev
            prev = new_node
            add = add // 10
        
        return prev