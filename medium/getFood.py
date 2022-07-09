class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        """
        #: food cell
        O: free space
        X: obstacle
        
        """
        
        queue = deque()
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    queue.append(((r,c),0))
                    break
                    
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # Perform a BFS
        while queue:
            curr = queue.popleft()
            r = curr[0][0]
            c = curr[0][1]
            print(r,c,curr[1])
            for i,j in directions:
                new_r = r + i
                new_c = c + j

                # Boundary checking
                # Issue found earlier: we have to mark the cell visited so that we do not revisit again when we are doing BFS
                # Make sure to check that if current cell is already visited, do not do anything. Otherwise, it will keep appending the visited cells to the queue and we have never-ending loop.
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != 'X' and grid[new_r][new_c] != "v":
                     # Food court
                    if grid[new_r][new_c] == "#":
                        return curr[1] + 1
                     # Empty space
                    grid[new_r][new_c] = "v" # Mark visited so that we do not revisit this cell again
                    queue.append(((new_r,new_c),curr[1] + 1))
                    
                    
                
                    
                
        return -1
                    
                    
                    
            
                        
