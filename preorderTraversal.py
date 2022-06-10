# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # Global array
    
    def preorder_helper(self,root,arr):
        
        if root == None:
            return
        arr.append(root.val)
        self.preorder_helper(root.left,arr)
        self.preorder_helper(root.right,arr)
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.preorder_helper(root,arr) # Pass by reference so that helper method can access the array memory to append value
        return arr


        
        
