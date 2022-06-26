# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def preorder_traversal(self,nums,left,right):
        
        # No elements available (Base case). There is never a case where right > left
        if left > right:
            return None
        
        mid = (right + left) // 2
        root = TreeNode(nums[mid])
        root.left = self.preorder_traversal(nums,left,mid - 1)
        root.right = self.preorder_traversal(nums,mid + 1,right)
        return root 
        
        
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        left = 0
        right = len(nums) - 1
        return self.preorder_traversal(nums,left,right)
        
