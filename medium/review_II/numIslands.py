class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # Note: this visited is not the same as BFS so do not get confused
        # The reason we need to keep track of visited cells because of the nature of the problem
        
        def bfs(r,c,rows,cols,grid,visited):
            # Boundary checking
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            # If the current cell is not an is land or we have already visited, then do not search
            if grid[r][c] == "0" or visited[r][c] == True:
                return
        
            # If we reach here, we haven't visited this cell and this cell is an island itself, we need to search furthermore
            visited[r][c] = True # Mark it visited
            bfs(r-1,c,rows,cols,grid,visited) # North
            bfs(r+1,c,rows,cols,grid,visited) # South
            bfs(r,c-1,rows,cols,grid,visited) # West
            bfs(r,c+1,rows,cols,grid,visited) # East
            
            
            
            
            
        rows = len(grid)
        cols = len(grid[0])
        numbIslands = 0
        
        # It is critical to keep track of visited cells since we do not want to overcount it
        visited = [[False for c in range(cols)] for r in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                # Search as soon as it is an island and has not yet been visited
                if grid[r][c] == "1" and visited[r][c] == False:
                    numbIslands += 1
                    bfs(r,c,rows,cols,grid,visited)
                else:
                    continue
                    
        return numbIslands        
        
