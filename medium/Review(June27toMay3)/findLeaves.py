# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Height of the tree is an important key here
        # Find the maxmimum height of the tree
        # Preorder DFS
        dict = defaultdict(list)
        
        def dfs(root):    
            
            if not root:
                return 0
            
            if root.left == None and root.right != None:
                maxHeight = 1 + max(0,dfs(root.right))
            elif root.left != None and root.right == None:
                maxHeight = 1 + max(0,dfs(root.left))
            else:
                # Full Tree
                maxHeight = 1 + max(dfs(root.left),dfs(root.right))
                
            dict[maxHeight].append(root.val)
            
            return maxHeight
        
        dfs(root)
        
        return dict.values()
            
            
            
        
