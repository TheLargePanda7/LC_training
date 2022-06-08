# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def helper(self,p,q):
        if p == None and q == None:
            # Both nodes are null is fine
            return True
        elif p == None or q == None:
            # One of the nodes is null (they share different structure)
            return False
        elif p.val == q.val:
            return self.helper(p.left,q.left) and self.helper(p.right,q.right)
        else:            
            return False
    
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        
        return self.helper(p,q)
        
        
    
            
                
            
            
        
