class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        visited = []
        queue = deque()
        cnt = 0
        # Create graph
        for src,dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
            
        # BFS
        # Need an extra for loop because there may be multiple graphs (disconnected situation)
        for i in range(n):
            curr_node = i
            if curr_node not in visited:
                queue.append(curr_node)
                visited.append(curr_node)
                while queue:
                    pop_node = queue.popleft()
                    for neighbor in graph[pop_node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.append(neighbor)
                        else:
                            continue
                cnt += 1
        """
        DFS Solution - Need to create helper method since it is recursive
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    dfs(neighbor)
                    
            return 1
            
        
        cnt = 0
        visited = []
        for i in range(n):
            curr_node = i
            if curr_node not in visited:
                cnt += dfs(i)
                
        return cnt
        
        """
            
        return cnt
