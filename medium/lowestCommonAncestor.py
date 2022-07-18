"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        
        p_ptr = p
        q_ptr = q
        
        path_p = []
        path_q = []
        
        # Construct the path from node p or q to root
        while p_ptr:
            path_p.append(p_ptr)
            p_ptr = p_ptr.parent
            
        while q_ptr:
            path_q.append(q_ptr)
            q_ptr = q_ptr.parent
        
        # Searching for the first common element in both arrays
        for i in range(len(path_q)):
            if path_q[i] in path_p:
                return path_q[i]
        
                
        
        
                
        
        
        
            
        
