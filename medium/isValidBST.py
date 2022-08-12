# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        arr = []
        def dfs_inorder(root):
            if not root:
                return
            dfs_inorder(root.left)
            arr.append(root.val)
            dfs_inorder(root.right)
            
        dfs_inorder(root)
        
        if len(arr) == 1:
            return True
        
        for i in range(len(arr)):
            if i < len(arr) - 1:
                if arr[i] < arr[i+1]:
                    continue
                else:
                    return False
        return True
