class Solution(object):
    
    def dfs(self,grid,row,col,r,c):
        # Boundary checking
        
        #print(r,c)
        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != "1":
            return
        
        # Only mark island to be visited if it is exactly equal to one
        grid[r][c] = "-1" # -1 as visited
        
        # Mark all neighbors of "1" to be visited
        self.dfs(grid,row,col,r-1,c) # Search north        
        self.dfs(grid,row,col,r,c-1) # Search west
        self.dfs(grid,row,col,r+1,c) # Search south
        self.dfs(grid,row,col,r,c+1) # Search east
        
        
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        """
        Observation:
        If grid[i][j] is "1", then it is an island by itself. However, it is connected with its neighbor(s) horizontally or vertically, it can be formed with a bigger version of island, but the count is still 1.
        
        Idea:
        We will iterate through the entire grid and check if the current element is 1. If it is exactly equal to 1, then we will increment the counter of islands. Otherwise, we skip.
        However, we need to somehow keep track of the visited elements and this can be done by DFS.
        
        Our DFS helper method will check the current element at index i and j to see if it is exactly equal to 1, if it is we will mark it as visited with a value of "0" or "-1" (Anything but 1) then recursively call the DFS helper method for repeating the same process of neighbor elements
        
        The index of neighbot elements can be shown below:
        
                    N (i-1,j)
                       |
          S (i,j-1) - "1" (i,j) - E (i,j+1)
                       |
                    S (i+1,j)
        * Remember to check the boundary.
                    
                    
               
        By using DFS, we will mark all neighbor elements visited so that next time when we encounter the same index i,j, we can just skip it instead of overcounting
        
        """
        if not grid or len(grid) == 0:
            return 0
        
        islands_cnt = 0
        cols = len(grid[0])
        rows = len(grid)
        
        
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # Grid[i][j] == 1
                    islands_cnt += 1
                    
                    # Call a dfs helper method to mark all neighbor nodes (including current node) to be visited
                    self.dfs(grid,rows,cols,r,c)
                
                    
                    
                    
                    
        return islands_cnt
    
                
        
        
        
        
