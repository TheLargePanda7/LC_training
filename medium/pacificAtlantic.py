class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Trick:
        For each current cell that we check, instead of asking "Can we reach neighbor cells from this current cell?" we ask "can neighbor cells reach this current cell?"
        With this, it is much easier to work with (top-down approach)
        
        """
        
        
        def bfs(queue,directions,rows,cols):
            # Visited array serves two purposes:
            # 1. Avoid revisiting cells
            # 2. Keep track of cells that can reach to pacific or atlantic ocean
            visited = []
            while queue:    
                r,c = queue.popleft()
                if (r,c) not in visited:
                    visited.append((r,c))
                elif (r,c) in visited:
                    continue
                    
                
                for direction in directions:
                    new_r = r + direction[0]
                    new_c = c + direction[1]
                    if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                        continue
                    # This is where the trick is
                    if heights[r][c] <= heights[new_r][new_c]:
                        # neighbor with (new_r,new_c) can reach current cell (r,c)
                        queue.append((new_r,new_c))
                    elif heights[r][c] > heights[new_r][new_c]:
                        # Not possible for neighbor cell to reach current cell
                        # Do not bother to count it
                        continue
            return visited
                
                
            
            
            
        rows = len(heights)
        cols = len(heights[0])
        atlantic_q = deque()
        pacific_q = deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        # Append coordinate of all cells that located within pacific ocean and vice versa
        # Those cells are used as a base case to check if neighbor cells can reach them. If so, neighbor cells must be possible to flow to pacific ocean
        for r in range(rows):
            pacific_q.append((r,0))
            atlantic_q.append((r,cols-1))
        
        for c in range(cols):
            pacific_q.append((0,c))
            atlantic_q.append((rows-1,c))
        
        
        # Contain coordinate of cells that can flow to pacific ocean
        pacific_res = bfs(pacific_q,directions,rows,cols)
            
        # Contain coordinate of cells that can flow to atlantic ocean
        atlantic_res = bfs(atlantic_q,directions,rows,cols)
        
        # Cells that overlap between atlantic and pacific res array will be cells that can flow to both pacific and atlantic oceans
        return list(set(pacific_res).intersection(set(atlantic_res)))
            
            
            
        
        
                                
        
        
