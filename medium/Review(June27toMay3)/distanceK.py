# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Reviewed
    def createGraph(self,root,dict,parent):
        if not root:
            return
        if parent:
            dict[root].append(parent)
        if root.left:
            dict[root].append(root.left)
            
        if root.right:
            dict[root].append(root.right)
        self.createGraph(root.left,dict,root)
        self.createGraph(root.right,dict,root)
        
        
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        
        """
        Since it is not possible for us to reach the parent node from the target node, we can just create a graph based on the tree and then use a BFS (with queue usage) to find the distance from target nodes to all neighbors node and append the nodes to the array when distance == k
        """
        dict = defaultdict(list)
        self.createGraph(root,dict,None)
        queue = deque()
        visited = []
        queue.append((target,0))
        res = []
        
        while queue:
            node,dist = queue.popleft()
            visited.append(node)
            if k == dist:
                res.append(node.val)
            for neighbor in dict[node]:
                if neighbor not in visited:
                    queue.append((neighbor,dist+1))
        
        return res
            
        
        
        
        
