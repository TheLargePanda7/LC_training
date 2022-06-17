# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def leavesSearcher(self,root,dict):
        if root.left == None and root.right == None:
            curr_height = 0
            if curr_height not in dict:
                # First appearance
                dict[curr_height] = [root.val]
            else:
                dict[curr_height].append(root.val)
            return curr_height
        if root.left == None:
            curr_height = 1 + max(0,self.leavesSearcher(root.right,dict))
        elif root.right == None:
             curr_height = 1 + max(self.leavesSearcher(root.left,dict),0)
        else:
            curr_height = 1 + max(self.leavesSearcher(root.left,dict),self.leavesSearcher(root.right,dict))
        if curr_height not in dict:
            # First appearance
            dict[curr_height] = [root.val]
        else:
            dict[curr_height].append(root.val)
        
        return curr_height
        
                
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
            Strategy
            Suppose we have this tree:
            
                 1
              /     \
             2       3
            / \    
           4  5
           We will compute the height for each node in the tree above, which gives us:
           Node 1 = height of 2
           Node 2 = height of 1
           Node 3, 4, and 5 = height of 3
           
           This is computed by using the following formula:
           Height(root) = 1 + max(height(root.left), height(root.right))
           
           Notice that the level height of the leaf nodes are grouped together in the final answer of [[3,4,5], [2], [1]]
           
           We do not need to actually remove the nodes, but only obtain the level of each node and group them accordingly based on their levels
           It is important to use an index to keep track of the level to append it to the dictionary
           For example,
           dict = {
            height = 0: [3,4,5]
            height = 1: [2]
            height = 2: [1]
        }
        """
        
        if root.left == None and root.right == None:
            # Only one node
            return [[root.val]]
        if root == None:
            # Empty tree
            return []
        
        dict = {}
        
        self.leavesSearcher(root,dict)
        
        res = []
        for key in dict:
            res.append(dict[key])
        return res
            
