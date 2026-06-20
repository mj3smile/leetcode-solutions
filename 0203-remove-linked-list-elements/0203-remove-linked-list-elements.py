# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode()
        curr = result
        while head:
            if head.val != val:
                curr.next = head
                curr = curr.next
            if head.next == None:
                curr.next = None
            head = head.next
        
        return result.next