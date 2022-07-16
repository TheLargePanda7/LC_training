"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        
        # DFS preorder fashion
        def dfs(curr,prev):
            # If we are at the null node, then just return the parent node
            # May be two cases: 1. parent node does not have child node, then just return parent node OR 2. we are at the last node in the last level and there is no other nodes to traverse, then just return a most recently traversed node, which is a parent node
            if not curr:
                return prev
            
            if prev:
                # Connect the child node with its parent
                # prev = parent node
                # curr = child node
                curr.prev = prev
                prev.next = curr
                
            # Keep track of the next node so that we can connect the last node in last level with the next node of parent node in current level
            next_node = curr.next
            
            # Traverse to the last level
            # If at last level, traverse to the last node of the last level
            # Make current node to be a parent node since we are moving to lower level
            last_node = dfs(curr.child,curr)
            
            # Remember to set the child pointer to be none 
            # Only do this after getting a last node. Otherwise, we cannot access the child node
            curr.child = None
            
            # Now begin flattening the linked list by connecting the next node with the last node in lowest level
            return dfs(next_node,last_node)
            
        
            
                
        
        root = head
        dfs(root,None) # -> return a pointer to a last node in flatten linked list
        return head 
        
