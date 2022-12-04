# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(next=head)
        p = result
        
        while p.next and p.next.next:
            previous = p
            first, second = p.next, p.next.next
            
            next_node = second.next
            previous.next = second
            first.next = next_node
            second.next = first
            p = first
        
        return result.next