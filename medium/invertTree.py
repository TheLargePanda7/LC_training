# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def (self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        queue = deque()
        res = root
        queue.append(root)
        left = None
        right = None
        
        while queue:
            n = len(queue)
            for i in range(n):
                pop_node = queue.popleft()
                if pop_node.left:
                    queue.append(pop_node.left)
                    left = pop_node.left
                if pop_node.right:
                    queue.append(pop_node.right)
                    right = pop_node.right
                pop_node.left = right
                pop_node.right = left
                left = None
                right = None
        
        return res
