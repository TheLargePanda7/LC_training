class Solution(object):
    
    # A helper method to top-sort the graph using stack
    def topSortDFS(self,stack,visited,graph,node):
        visited[node] = True
        
        for neighbor in graph[node]:
            if visited[neighbor] == False:
                self.topSortDFS(stack,visited,graph,neighbor)
        
        stack.append(node)
        
    # A helper method to traverse the graph using DFS and mark the path
    # WHITE -> unvisited
    # GRAY -> visiting
    # BLACK -> finished visiting
    # If we detect gray in the middle of the way, we are having a cycle
    def dfs(self,graph,node_status,i):
        node_status[i] = "GRAY"
        
        for neighbor in graph[i]:
            if node_status[neighbor] == "GRAY":
                # Detected cycle
                return True
            elif node_status[neighbor] == "WHITE":
                if self.dfs(graph,node_status,neighbor):
                    return True
        
        # Finish line (# If we get to this point, that means no cycle has been detected, so return false)
        node_status[i] = "BLACK"
        return False
    
    # A helper method to check if there is a cycle
    def cycleDetector(self,graph,n):
        node_status = ["WHITE" for i in range(n)]
        
        for i in range(n):
            if node_status[i] == "WHITE":
                if self.dfs(graph,node_status,i):
                    return True
        
        return False
                
                
            
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        """
        n = 2 prerequisites = [[1,0]]
        
        there are two possible courses 0 and 1 (n-1)
        From the given array, to take course 1, we must take course 0 
        
        return array = [0,1]
        
        Initial thought:
        From the look of this problem, this is a graph problem as each course represents a node and prerequisite represents an edge from one node to another
        This is also a topological sort problem, which is potentially the answer for this problem. Imagine we have a directed graph, our goal is to order the nodes such that it can go from left to right along with edges
        For example:
        0 -> 1 -> 3
        |
        2
        Topological order can be:
        0 -> 2 -> 1 -> 3
        We can see that we organize the nodes such that edges going from left to right
        
        First, we would need to create a graph based on the given array and this can easily be done using dictionary
        Create necessary DS (queue, array, set, etc) and apply DFS to create topological order
        To keep track if there is a cycle in the graph, mark nodes to be visiting and only mark nodes to be visited when the recursion of traversal is done. If we detect the visiting node again on the way, we detect a cycle
        """
        
        
        # Create a graph using dictionary
        graph = defaultdict(list)
        
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        # Before we perform top-sort, we need to check if it has a cycle
        if self.cycleDetector(graph,numCourses):
            return []
        
        # Need to keep track of visited nodes 
        visited = [False for i in range(numCourses)]
        stack = []
        
        # i: 0 -> n - 1
        for node in range(numCourses):
            if visited[node] == False:
                self.topSortDFS(stack,visited,graph,node)
        
        # The stack we have will always be opposite of what we want
        # Use index slicing to get the reversed order 
        return stack[::-1] 
                
        
                
        
        
        
        
        
        
        
        
            
                
            
            
                
        
        
        
