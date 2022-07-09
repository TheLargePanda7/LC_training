class Solution(object):
    # Note: reviewed, but still need to practice more to remember the structure of the algorithm
    def dfs(self,graph,currNode,mark):
        
        mark[currNode] = "GRAY"
        
        for neighbor in graph[currNode]:
            if mark[neighbor] == "GRAY":
                return True
            elif mark[neighbor] == "WHITE":
                # Check further the neighbor
                if self.dfs(graph,neighbor,mark):
                    return True
                
        mark[currNode] = "BLACK"
        return False
        
    def cycleDetector(self,graph,n,mark):
        # We need to iterate through every single node because there may be the case that one graph is completely separated from other graph and it has cycle. We need to make sure we check that
        for node in range(n):
            if mark[node] == "WHITE":
                if self.dfs(graph,node,mark):
                    return True
                
        return False
            
        
    
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        """
        From the look at this problem, we cannot finish all courses if there is a contradiction meaning that two courses depend on each other. For example, we can take course 1 if we take course 2, but cannot take course 2 without finishing course 1. 
        If we were to transform this into a graph problem, such impossibility happens when there exists a cycle in the graph. If it does not exist a cycle, we are good to complete all courses
        So we will:
        1. Transform this into a graph using dictionary
        2. Write a simple helper method to DFS and check if there is a cycle
        -Can accomplish this by marking/updating color of each node as we traverse
            -> If we are traversing, mark node to be visiting
            -> If we did not visit the node yet, mark it
            -> If we are done traversing, mark it to be visited
            Hence, we will have three different colors to represent its state
            If we encounter a visiting node during traversal, we know there is a cycle
        """
        
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        
        
        """
        WHITE: "not yet visited"
        GRAY: "visiting"
        BLACK: "visited"
        if we encounter a visiting node on the path, we detected a cycle
        """
        mark = ["WHITE" for i in range(numCourses)]
        
        if self.cycleDetector(graph,numCourses,mark):
            return False
        return True
        
