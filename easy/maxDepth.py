# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # max height -> max depth
        def maxHeight(root):
            if not root:
                return 0
            height = 0
                
            if root.left != None and root.right == None:
                height = 1+ max(maxHeight(root.left),0)
            elif root.left == None and root.right != None:
                 height = 1+ max(maxHeight(root.right),0)
            else:
                height = 1 + max(maxHeight(root.left),maxHeight(root.right))
            
            
            return height
        
        max_height = maxHeight(root)
        return max_height
    
