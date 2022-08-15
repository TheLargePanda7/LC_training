"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        # Base case
        if not node:
            return node
        
        
        queue = deque()
        # key = actual reference, value = clone
        copied = {} 
        

        queue.append(node)
        # Clone start node
        clone_node = Node(node.val,[])
        copied[node] = clone_node
        ret_node = clone_node
        
        
        
        # BFS
        while queue:
            curr = queue.popleft()
            
            # curr.neighbors is a list
            for neighbor in curr.neighbors:
                # If this neighbor node has not yet been cloned, we need to clone it and mark it cloned so that we can reference it next time
                if neighbor not in copied:
                    queue.append(neighbor)
                    # Clone it
                    clone_node = Node(neighbor.val,[])
                    copied[neighbor] = clone_node
                    
                # Original: we have "if neighbor in copied" is not correct because this will prevent us from making connection from curr node to neighbor node after neighbor node is cloned.
                # This neighbor has already been cloned
                # Add the clone version of neighbor to the current node
                clone_node = copied[neighbor]
                # curr -> current visited node
                copied[curr].neighbors.append(clone_node)
                    
                    
        return ret_node
                    
                    
                    
            
            
            
                    
                    
                
            
            
        
