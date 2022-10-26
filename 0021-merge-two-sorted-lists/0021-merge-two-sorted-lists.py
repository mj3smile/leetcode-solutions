# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        p = result
        
        while list1 or list2:
            if list1 and not list2:
                p.next = list1
                break
            if list2 and not list1:
                p.next = list2
                break
                
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            
            p = p.next
            
        return result.next
        