class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        """
        Start: 6:14
        Idea:
        1. Make graph based on adjcent list
        2. Declare an array with n - 1 elements marked with WHITE
        3. Perform DFS starting with node 0
        4. Mark node to be black if we are done traversing from root to leaf
        5. Mark node to be gray if we are visiting
        6. f we encounter GRAY node during traversal, return False
        
        """
        
        def dfs(node,prev):
            
            if node in visited:
                return False
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                    
                if not dfs(neighbor,node):
                    return False
                
                
            
            return True
            
            
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            start = edges[i][0]
            end = edges[i][1]
            
            # Undirected graph
            graph[start].append(end)
            graph[end].append(start)
        
        visited = []
        
        return dfs(0,-1) and len(visited) == n
