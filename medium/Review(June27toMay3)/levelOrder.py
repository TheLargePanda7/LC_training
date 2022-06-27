# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        Observation:
        
        Recall that Level Order Traversal requires a queue to implement (FIFO)
        
        The algorithm is as follow:
        1. Enqueue an element to the queue
        2. Iterate through the current number of elements in the queue
            For each of them:
                we dequeue and check if the node is null (it is possible to have such situation)
                if it is not null, we can push the value of the node to the temporary array and enqueue its children to the queue (Note this does not affect our inner loop because the length of our queue was pre-defined earlier)
            Once inner loop is done, that signals that level i is done, then just append to the res array
        """
        if not root:
            return []
        
        
        queue = deque()
        res = []
        
        queue.append(root)
        
        # BFS traversal
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue.popleft() # pop the first in element in the queue
                if node:
                    # Important to add in such order (left to right)
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            # Once inner loop finishes, we are also done with level i
            res.append(level)
        
        # We want to return the res array except the last element
        # This is because we also append null nodes to the queue, so the while loop will still iterate although we do not necessarily need it
        # Hence, we sort of append the empty sub array for no reason to the res array and the empty subarray is the last element in the res array
        return res[:len(res)-1]


        
        
        
        
