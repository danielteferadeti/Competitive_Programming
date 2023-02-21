# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        _dict = {}
        
        intersect = None
        while headA:
            _dict[headA] = headA
            headA = headA.next
            
        while headB:
            if headB not in _dict:
                _dict[headB] = headB
                headB = headB.next
            else:
                intersect = headB
                break
        
        return intersect