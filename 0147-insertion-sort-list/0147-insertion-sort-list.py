# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        new.next = head
        
        items = [new]
        curr = head
        while curr:
            items.append(curr)
            curr = curr.next
        
        for i in range(1, len(items)):
            prev1, next1 = items[i - 1], None
            if i < len(items) - 1:
                next1 = items[i + 1]
            
            j = i
            while j > 1 and items[j - 1].val > items[j].val:
                items[j], items[j - 1] = items[j - 1], items[j]
                j -= 1
            
            if j == i:
                continue
            
            prev1.next = next1
            prev2, next2 = items[j - 1], None
            if j < len(items) - 1:
                next2 = items[j + 1]
            
            prev2.next = items[j]
            items[j].next = next2
        
        return new.next