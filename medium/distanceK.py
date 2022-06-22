# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    def graphCreation(self,root,graph,predecessor):
        if not root:
            return
        if predecessor:
            graph[root].append(predecessor)
            
        if root.right:
            graph[root].append(root.right)
            self.graphCreation(root.right,graph,root)
        if root.left:
            graph[root].append(root.left)
            self.graphCreation(root.left,graph,root)
        
        
            
            
        
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        
        
        """
        
        Given a tree where root = [3,5,1,6,2,0,8,null,null,7,4]
        We can convert to graph following below:
        
        graph[3] = [5,1]
        graph[1] = [3,0,8]
        graph[5] = [3,6,2]
        graph[6] = [5]
        and so on
        
        From here, we can just perform bfs on the graph and then we are done
        
        Example: 
        queue = [(5,0)]
        if d == K:
            res.append(node)
        
        for neighbor in graph[5]:
            if neighbor not in visited:
                queue.append((neighbor,d+1)) # traverse to the next node in the graph
                
        queue = [(2,1),(6,1),(3,1)]
        
        queue = [(7,2),(4,2),(6,1),(3,1)] 
        
        
        """
        
        res = []
        graph = defaultdict(list)
        queue = deque()
        visited = set()
        
        # Convert tree to graph to inherit the edge-bidirection properties
        # That way we can traverse as we want to find the distance k from target node
        
        self.graphCreation(root,graph,None)
        
        # Getting started with target node
        queue.append((target,0)) # target is a node, not just a value
        
        while queue:
            node,distance = queue.popleft()
            visited.add(node)
            
            # distance is accumulated as we traverse through nodes in the graph, if current distance (distance from target node) is exactly what we want, so this is the node we want to append
            if distance == k:
                res.append(node.val)
            
            # For each neighbor of the current node, we want explore them as long as they are not yet visited. 
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor,distance+1))
        
        return res
                
            
        
        
        
