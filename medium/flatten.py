"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        """
        The important key point to notice in this problem is that we can turn multilevel linked list into a binary tree problem by rotating the image by 90 degree where next ptr = right ptr and child ptr = left ptr. Another thing is that if we perform the preorder DFS on this tree, we get exactly the order we want when we flatten the linked list
        Remember how we write code to recursively travere the binary tree in preorder fashion, do the same in this problem except we need to keep track of the previous node in order to establish connection
        
        """
        # Preorder - Traversal
        def dfs(root,prev):
            if not root:
                return prev
            
            
            # Establish the connection of the current node with the previous node in the flatten linked list
            if prev:
                 # Connect linked list nodes
                root.prev = prev
                prev.next = root
            
            # We must get a hold of this variable before losing its ptr (we lose ptr of next node of root once we get a tail node)
            root_next = root.next
            
            tail = dfs(root.child,root) # Left = child - this recursive function returns a ptr to the tail of the linked list
            root.child = None
            return dfs(root_next,tail) # we now can connect the tail and the other portion on higher level together
            
            
            
        root = head
        dfs(root,None)
        return head
    
        
        
        
