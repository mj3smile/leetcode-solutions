# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        index = dict()
        sorted_list = list()
        
        for l in lists:
            head = l
            while head:
                next_node = head.next
                head.next = None
                index[head.val] = index.get(head.val, [])
                index[head.val].append(head)
                sorted_list.append(head.val)
                head = next_node
        
        sorted_list.sort()
        result = ListNode()
        r = result
        for l in sorted_list:
            r.next = index[l][-1]
            index[l].pop()
            r = r.next
        
        return result.next