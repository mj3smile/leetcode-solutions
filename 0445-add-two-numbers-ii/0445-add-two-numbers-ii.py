# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_nodes = list()
        l2_nodes = list()

        while l1 or l2:
            if l1:
                l1_nodes.append(l1)
                l1 = l1.next
            if l2:
                l2_nodes.append(l2)
                l2 = l2.next
        
        result = None
        remainder = 0
        while l1_nodes or l2_nodes or remainder > 0:
            one, two = 0, 0
            if l1_nodes:
                n = l1_nodes.pop()
                one = n.val
            if l2_nodes:
                n = l2_nodes.pop()
                two = n.val
            
            add = one+two+remainder
            if add > 9:
                remainder = add // 10
                add = add % 10
            else:
                remainder = 0

            new = ListNode(val=add)
            new.next = result
            result = new
        
        return result