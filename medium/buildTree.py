# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_mp = {}
        n = len(inorder)
        for i in range(n):
            if inorder[i] not in inorder_mp:
                inorder_mp[inorder[i]] = i
        
        
        def treeConstruction(L,R):
            nonlocal preorder_i
            
            # Base case (either the left or right subtree, the L ptr will eventually pass R ptr) to signal that there are no more nodes to build
            if L > R:
                return None
            
            root = TreeNode(preorder[preorder_i])
            preorder_i += 1
            
            # Left subarray not including root
            root.left = treeConstruction(L,inorder_mp[root.val] - 1)
            
            # Right subarray not including root
            root.right = treeConstruction(inorder_mp[root.val] + 1,R)
            
            
            return root
            
        preorder_i = 0  
        return treeConstruction(0,n-1)    
        
        
