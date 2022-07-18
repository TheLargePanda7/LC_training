# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        Inorder: LEFT ROOT RIGHT
        1 2 3 4 5 6
        """
        res = []
        
        def inorderDFS_traversal(root):
            if not root: 
                return
            inorderDFS_traversal(root.left)
            res.append(root)
            inorderDFS_traversal(root.right)
            
        inorderDFS_traversal(root)
        
        index_successor = res.index(p)
        if index_successor == len(res) - 1:
            return None
        
        return res[index_successor+1]
        
        
        
        
        
            
                
            
