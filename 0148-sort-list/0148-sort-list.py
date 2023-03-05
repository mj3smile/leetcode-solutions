# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(head):
            # arr = []
            # c = head
            # while c:
            #     arr.append(c.val)
            #     c = c.next
            # print(arr)
            
            if not head or not head.next:
                return head
            
            slow, fast = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            
            second_half = slow.next
            slow.next = None
            head1 = mergeSort(head)
            head2 = mergeSort(second_half)
            
            dummy = ListNode()
            d = dummy
            while head1 or head2:
                if not head1:
                    d.next = head2
                    head2 = head2.next
                    d = d.next
                    continue        
                if not head2:
                    d.next = head1
                    head1 = head1.next
                    d = d.next
                    continue
                    
                if head2.val < head1.val:
                    d.next = head2
                    head2 = head2.next
                else:
                    d.next = head1
                    head1 = head1.next
                d = d.next
            
            return dummy.next
        
        return mergeSort(head)
            