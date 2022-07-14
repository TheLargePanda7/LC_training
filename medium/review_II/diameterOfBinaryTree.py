# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def depth(root):
            if not root:
                return 0
            nonlocal diameter
            left_depth = depth(root.left)
            right_depth = depth(root.right)
    
            # There may be the case that the maximum path does not involve the root node. Hence, we need to keep track of the best possible maximum depth that we have searched so far to account for this
            # Path = left_depth + right_depth
            diameter = max(diameter,left_depth + right_depth) # If the current discovered path is larger, take it
            return 1 + max(left_depth,right_depth) # Return the current depth to recursive function
        
        depth(root)
        return diameter
            
        
    
            
        
        
        
        
