# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        """
        The conventional way to delete a node would fail here because we do not have access to the head.
        A clever way to do this (suggested by Leetcode community) is to change the value instead of removing it
        
        For example, suppose we have:
        4 -> 5 -> 1 -> 9
        Where 5 is given node
        
        We change the value of 5 to be the value of its next node
        
        4 -> 1 -> 1 -> 9
        
        From here we can remove the second node with value of 1 instead of the given node, which gives us:
        4 -> 1 -> 9
        
        As we see, we did not delete the given node, but instead its next node by first replacing given node value
        """
        
        if node.next.next != None:
            
            temp = node.next.next
        
            node.val = node.next.val
        
            node.next = temp
            
        elif node.next.next == None:
            
            node.val = node.next.val
            node.next = None

        
