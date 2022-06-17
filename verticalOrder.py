# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        # We need to get the actualy range of column so that we can easily iterate through later
        min_col = 0
        max_col = 0
        #-------------------------------Helper function end-------------------------------
        def traverse(container,root,row,col):
        
            if not root:
                return
            else:
                nonlocal min_col, max_col

                """
                    If nodes with value of 1 and 2 are in the same group (col = 0),
                    we know that they must be in the same array of column 0
                    container = {
                        "0": [(0,2),(2,1)]
                    }

                """
                # Append the column of the located node as a key
                # And then its row and actual value in a tuple as a key-value
                if col not in container:
                    container[col] = [(row,root.val)]
                else:
                    # Node with the same column
                    container[col].append((row,root.val))

                # Next step is to obtain the range of cols to use for iteration later
                min_col = min(min_col,col)
                max_col = max(max_col,col)


            # Make sure to do left before right in case they share the same i and j index    
            traverse(container,root.left,row+1,col-1)
            traverse(container,root.right,row+1,col+1)
        #-------------------------------Helper function end-------------------------------
        
        container = {}
        res = []
        #container[3] = (1,1)
        
        traverse(container,root,0,0)
        print(min_col,max_col)
        
        # Iterate from the left to right to collect nodes in the same column into array
        for i in range(min_col,max_col+1):
            # remember that container[i] gives us [(row,val),(row,val),...]
            # We need to give priority for the top node, so we need to sort based on the first element in tuple since it represents the row value
            container[i].sort(key = lambda item:item[0])
            
            # We only need to append the value of the node not the row, so we need to filter it out
            res.append([value for row,value in container[i]])
        return res
        
