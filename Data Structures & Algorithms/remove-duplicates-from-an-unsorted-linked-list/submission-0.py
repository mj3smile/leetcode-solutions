# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq = dict()

        curr = head
        while curr:
            freq[curr.val] = freq.get(curr.val, 0) + 1
            curr = curr.next
        
        result = ListNode()
        result.next = head

        prev = result
        curr = head
        while curr:
            if freq[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return result.next