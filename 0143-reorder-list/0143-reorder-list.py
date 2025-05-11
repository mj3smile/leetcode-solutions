# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return

        nodes = list()
        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        prev, curr = head, head.next
        while curr:
            last = nodes.pop()
            if prev == last:
                prev.next = None
                break
            if curr == last:
                curr.next = None
                break
            
            print(curr.val, last.val)
            prev.next = last
            last.next = curr
            prev, curr = curr, curr.next
        
        return