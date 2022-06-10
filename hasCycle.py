# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        
        turtle = head
        rabbit = head.next
        
        while rabbit != turtle:
            if rabbit == None or rabbit.next == None:
                # Reached the end of linked list
                return False
            
            turtle = turtle.next
            rabbit = rabbit.next.next
        
        # If we reach here, rabbit == turtle -> there is a cycle
        return True
            
            
