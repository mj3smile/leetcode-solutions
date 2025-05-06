# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result

        while list1 or list2:
            if list1 and not list2:
                head.next = list1
                head = head.next
                list1 = list1.next
                continue

            if list2 and not list1:
                head.next = list2
                head = head.next
                list2 = list2.next
                continue

            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            
            head = head.next
        
        return result.next