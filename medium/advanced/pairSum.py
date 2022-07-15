# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        
        # Reverse linked list    
        def reverse(node):
            prev = None
            curr = node
            while curr:
                # Keep track of the next node to move forward
                forward_node = curr.next
                # Established linked list
                curr.next = prev
                
                # Keep track of the previous node to establish connection later
                prev = curr
                curr = forward_node
            
            return prev
                
        # Get the middle node using slow and fast pointers
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        head_l1 = head
        
        # slow = head of the second linked list (or upper middle element if number of nodes is even)
        head_l2 = reverse(slow)
        
        maxVal = 0
        
        # IMPORTANT: for this while loop, we must use head_l2 instead of head_l1 because head_l1 is still a whole linked list since we did not disconnect the next pointer anything;wheareas, head_l2 is only half after the reverse call. So we will have an error if we use head_l1
        while head_l2:
            # compute and keep the max
            maxVal = max(maxVal,head_l1.val + head_l2.val)
            # Move pointers of two linked lists at the same time
            head_l1 = head_l1.next
            head_l2 = head_l2.next
        
            
        
        return maxVal
        
        
