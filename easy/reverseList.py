# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        The idea is that we cannot go back to previous node since this is not a doubly linked list. In addition, once we make a pointer adjustment to point to the previous node, we lose track of the next node to move forward to. So we need to declare two pointers, one is to keep track of the previous node and the other one is to keep track of the next node so we can make adjustment.
        """
        prev = None
        curr = head
        ans = None
        while curr:
            next_n = curr.next
                
            curr.next = prev
            prev = curr
            curr = next_n
        
        return prev
    
        
