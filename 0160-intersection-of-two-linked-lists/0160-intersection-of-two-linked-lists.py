# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = dict()
        
        while headA:
            listA[headA.val] = listA.get(headA.val, list())
            listA[headA.val].append(headA)
            headA = headA.next
        
        while headB:
            if (headB.val not in listA) or (headB not in listA[headB.val]):
                headB = headB.next
                continue
            
            return headB
        
        return None