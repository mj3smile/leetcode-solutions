# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr = result

        while list1 or list2:
            if not list1 or (list2 and list2.val < list1.val):
                curr.next = ListNode(list2.val)
                list2 = list2.next
            else:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            curr = curr.next

        return result.next