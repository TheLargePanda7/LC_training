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
        mp = {}
        prev = None
        curr = head
        dummy = Node(-1)
        res = dummy
        
        while curr:
            new_node = Node(curr.val)
            mp[curr] = new_node
            dummy.next = new_node
            dummy = new_node
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random != None:
                curr_copy = mp[curr]
                curr_copy.random = mp[curr.random]
            curr = curr.next
                
