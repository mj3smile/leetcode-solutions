# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = 0
        h = head
        while h:
            length += 1
            h = h.next
        
        result = 0
        for i in range(length - 1, -1, -1):
            if head.val == 1:
                result += 2**i
            head = head.next
        
        return result
        