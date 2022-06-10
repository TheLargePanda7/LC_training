# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        """
            We declare two pointers: one is to keep track of the current node that we iterate and the other one is to keep track of the previous node in case we need to remove the current node so that we can adjust pointers accordingly. However, things become tricky if the head is what we want to remove. To solve this issue, we can declare a sentinel node, which acts as a pseudo-node, have it pointing to the head. So we do not care if we remove the head node because we simply just return sentinel.next at the end of the function
        
        """
        sentinel = ListNode(0) # Pseudo-node
        sentinel.next = head
        prev = sentinel
        temp = head
        while temp != None:
            if temp.val == val:
                prev.next = temp.next # Adjust pointer
                # Keep the previous pointer since we are not removing it
            else:
                prev = temp 
            
            temp = temp.next # Move on to the next node
        return sentinel.next
