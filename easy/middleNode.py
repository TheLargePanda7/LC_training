# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        curr = head
        R = 0
        L = 0
        
        # Traverse through linked list to get the index of the last node and total number of nodes
        while curr.next != None:
            curr = curr.next
            R += 1
        
        
        cnt = R + 1
        
        # Calculate the middle index
        middle = (R + L) // 2
        
        if cnt % 2 == 0:
            # Even (want to return the second middle node, so we increment index to be 1)
            middle += 1
        
        # Traverse again to actually return the middle node using middle index that we found
        curr_index = 0
        curr2 = head
        while curr2:
            if curr_index == middle:
                return curr2
            curr2 = curr2.next
            curr_index += 1
        
            
        
