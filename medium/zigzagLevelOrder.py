# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        """
        Observation:
        Zig Zag Order Traversal is essentially just a Level Order Traversal but we alternate the order as we go through level instead
        For example, if nodes are added from the left to the right order, in the next level, we will add nodes from right to left order and so on.
        We can use BFS (the same algorithm for level order traversal problem) and add a new variable to keep track of the current variable. If level is odd, we will append left. Otherwise, we will append right and so on
        """
        if not root:
            return []
        
        dict = defaultdict(deque)
        queue = deque()
        currLevel = 0
        queue.append(root)
        
        # BFS traversal
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node: 
                    if currLevel % 2 == 0:
                        dict[currLevel].append(node.val)
                    elif currLevel % 2 != 0:
                        dict[currLevel].appendleft(node.val)
                        
                    queue.append(node.left)
                    queue.append(node.right)
                
                    
            currLevel += 1        
            # Once inner loop finishes, we are also done with level i
            
            
        return dict.values() # Return an array of queues
        
        
