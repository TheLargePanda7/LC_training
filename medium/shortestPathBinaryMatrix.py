class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        """ 
            BFS solution
        """
        
        if grid[0][0] != 0:
            return -1
        # Special case where matrix is 1x1
        if len(grid) == 1:
            return 1
            
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        step = 1
        queue.append((0,0,step))
        # At the top left, there are only three neighbors
        directions = [(0,1),(1,1),(1,0)]
        for new_r,new_c in directions:
            if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols or grid[new_r][new_c] != 0:
                    continue
            queue.append((new_r,new_c,step+1))
            
            
                
        shortPath = 200
        while queue:
            #print(queue)
            r,c,step = queue.popleft()
            # north,south,west,east,north_east,north_west,west_south,east_south 
            directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,-1),(1,1)]
            for dr,dc in directions:
                new_r = r + dr
                new_c = c + dc
                # Check for boundary
                if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols or grid[new_r][new_c] != 0:
                    continue
                grid[new_r][new_c] = 1
                if new_r == rows - 1 and new_c == cols - 1:
                    #print('hello')
                    shortPath = min(shortPath,step+1)
                queue.append((new_r,new_c,step+1))
        if shortPath == 200:
            return -1
        return shortPath
        
        
        
        
        
        
        
        """
        DFS + Backtracking solution (TLE)
         rows = len(grid)
        cols = len(grid[0])
        
        shortestPath = 200
        def dfs(r,c,rows,cols,grid,step):
            nonlocal shortestPath
            
            # Check Boundary
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 0:
                return False
                
            # Base case + Destination
            if r == rows- 1 and c == cols - 1:
                #print(r,c,step,shortestPath)
                shortestPath = min(shortestPath,step)
                return True
            
            
            grid[r][c] = 1 # Mark current cell visited
            
            north = bfs(r-1,c,rows,cols,grid,step + 1)
            south = bfs(r+1,c,rows,cols,grid,step + 1)
            west = bfs(r,c-1,rows,cols,grid,step + 1)
            east = bfs(r,c+1,rows,cols,grid,step + 1)
            north_east = bfs(r-1,c+1,rows,cols,grid,step + 1)
            north_west = bfs(r-1,c-1,rows,cols,grid,step + 1)
            west_south = bfs(r+1,c-1,rows,cols,grid,step + 1)
            east_south = bfs(r+1,c+1,rows,cols,grid,step + 1)
            
            #Backtrack
            grid[r][c] = 0
            
            return north or south or west or east or north_east or north_west or west_south or east_south
        
        if dfs(0,0,rows,cols,grid,1):
            return shortestPath
        else:
            return -1
        """
       
                
        #for r in range(rows):
        #    for c in range(cols):
                
