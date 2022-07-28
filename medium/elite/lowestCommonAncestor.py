"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        We will obtain the path from p to root and q to root by traversing using self.parent pointer
        Store the paths into data strucutre such as arrays or strings
        Let's use example 2:
        path from p to root is 5 -> 3
        path from q to root is 4 -> 2 -> 5 -> 3
        
        Notice that the FIRST common point of these two paths is the LCA
        
        """
        
        curr_p = p
        curr_q = q
        path_p = []
        path_q = []
        
        # Iteratively construct the path
        while curr_p != None:
            path_p.append(curr_p)
            curr_p = curr_p.parent
        while curr_q != None:
            path_q.append(curr_q)
            curr_q = curr_q.parent
        
        # Traverse the array to find the FIRST common point
        # To find the intersection of two lists, we will go through one array in order and check if it is in other path. If it is, then return that element
        # This guarantee to get a first common point because we traverse and check elements from left to right
        
        for i in range(len(path_q)):
            if path_q[i] in path_p:
                return path_q[i]
            
            
        return None
            
            
        
