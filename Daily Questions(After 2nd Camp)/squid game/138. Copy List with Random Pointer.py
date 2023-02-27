"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_list = {}
        old_random = {}
        new_list = {}
        
        false_head, count = head, 1
        
        while false_head:
            old_list[false_head] = count
            count += 1
            false_head = false_head.next
            
        old_list[false_head] = count
        false_head = head
        
        while false_head:
            old_random[false_head] = old_list[false_head.random]
            false_head = false_head.next
        
        false_head, count, prev, new_head = head, 1, None, None
        while false_head:
            val = false_head.val
            
            new_node = Node(val)
            if not prev:
                prev = new_node
                new_head = new_node
                
                new_list[count] = new_node
                count += 1
                false_head = false_head.next
            else:
                prev.next = new_node
                prev = new_node

                new_list[count] = new_node
                false_head = false_head.next
                count += 1
            
        new_list[count] = None
        for node in old_random:
            node_with_rand = new_list[old_list[node]]
            rand_node = new_list[old_random[node]]
            
            node_with_rand.random = rand_node
        
        return new_head
        
        