# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cycle = 0
        list_elmnt = []
        true_head = head
        return_head = None
        
        if k==1:
            return head
        
        while head:
            list_elmnt.append(head.val)
            head = head.next
            
        head = true_head
        
        if len(list_elmnt) < k:
            return head
        
        cycle = len(list_elmnt)//k
        i = head
        prev = None
        start = i
        last_end = None
        while cycle > 0:
            count = 0
            while count < k:
                next_i = i.next
                i.next = prev
                prev = i
                i = next_i
                count += 1
            if not return_head:
                return_head = prev
            if not last_end:
                start.next = i
                last_end = start
                prev = None
                start = i
            else:
                start.next = i
                last_end.next = prev
                prev = None
                last_end = start
                start = i
            cycle -= 1
            
        return return_head