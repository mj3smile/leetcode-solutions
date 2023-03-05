# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(head):
            if not head or not head.next:
                return head
            
            # split into two halves
            slow, fast = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            
            first_half = head
            second_half = slow.next
            slow.next = None
            half1 = mergeSort(first_half)
            half2 = mergeSort(second_half)
            
            # merge and sort two halves
            dummy = ListNode()
            d = dummy
            while half1 or half2:
                if not half1:
                    d.next = half2
                    half2 = half2.next
                    d = d.next
                    continue        
                if not half2:
                    d.next = half1
                    half1 = half1.next
                    d = d.next
                    continue
                    
                if half2.val < half1.val:
                    d.next = half2
                    half2 = half2.next
                else:
                    d.next = half1
                    half1 = half1.next
                d = d.next
            
            return dummy.next
        
        return mergeSort(head)
            