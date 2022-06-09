# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    # Return boolean 
    def helper(self,root,target,curr):
        if root == None:
            return False
            
            
        if root.left == None and root.right == None:
            # Base case (Leaf Node)
            curr += root.val
            if curr == target:
                return True
            else:
                return False
        curr += root.val
        
        
            
        return self.helper(root.left,target,curr) or self.helper(root.right,target,curr) 
            
        
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        """
        General approach:
        Apply Depth-first search tree traversal and recursively pass 'curr' variable as we traverse to keep track of the current sum
        Once we reach the leaf, we can check if the current sum (added through the journey) is the same as target. If so, return true and otherwise return false
        If we reach the null node, we know that we must return false because it is not a valid path without the leaf node!
        """
        return self.helper(root,targetSum,0)
        
        
        
        
