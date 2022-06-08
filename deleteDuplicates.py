# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        Approach:
        Declare pointers P (to keep track of previous node) and T (to keep of current node)
        
        If T != P:
            P = T # Assign the previous node to be the current node
            T = T.next # Move on to the next node
        If T == P:
            P.next = T.next # Adjust the pointer of the previous to pointer to the next node of removed node
            T.next = null # Remove pointers of removed node
            T = P.next
        """
        """
        previous = None
        temp = head
        
        while temp != None:
            if previous == None:
                previous = temp
                temp = temp.next
            elif temp.val != previous.val:  
                previous = temp
                temp = temp.next
            else:
                previous.next = temp.next
                temp.next = None
                temp = previous.next
                
        return head
        
        """
        
        temp = head
        while temp != None and temp.next != None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next # Adjust the pointer
                # temp = temp.next Note: we do not want to move the temp pointer just yet because they may be more than two duplicated nodes
                # In this case, we will keep temp pointer at this current node and keep using it to eliminate all duplicated nodes
            else:
                # No duplicated node is detected, we are okay to continue searching...
                temp = temp.next
                
        return head
                
                
        
