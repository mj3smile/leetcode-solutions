# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        node1, node2 = head, head.next
        while node1 and node2:
            if node1 == node2:
                return True
            
            node1 = node1.next
            node2 = node2.next
            if node2:
                node2 = node2.next
        
        return False
