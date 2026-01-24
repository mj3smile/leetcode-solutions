# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = list()
        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next
        
        toRemove = len(arr) - n
        if toRemove == 0:
            return arr[toRemove].next  
        
        arr[toRemove - 1].next = arr[toRemove].next
        return head