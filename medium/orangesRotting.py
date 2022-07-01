class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        """
        It is important to observe that this problem involves BFS because for each rotten orange, we potentially visit all of its neighbor cells
        BFS usually involves queue usage
        
        Algorithms:
        1. Iterate through the entire grid and append the coordinate (r,c) to the queue if current orange is rotten. If it is a normal orange, we need to keep track the count of it otherwise we would not know if it is possible for an orange to not to be rotten (not reachable)
        2. For each element in the queue, we pop it out from the queue and check its neighbors (north,south,west,and east) and append to the queue
        Time Complexity:
        O(M X N)
        Space Complexity:
        O(M X N) - Worst case is that all oranges in the grid are all rotten
        
        """
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh_orange = 0
        timer = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_orange += 1
        # Need two conditions for the while loop
        # While loops continue as long as we still have rotten oranges to check for and the fresh orange is greater than 0 (there may be a case that we are at the last rotten orange, but there is no fresh orange left, then we can just stop the loop.Otherwise, timer will have one extra minute)
        
        while queue and fresh_orange != 0:
            
            curr_rotten_oranges = len(queue)
            timer += 1
            # For the current number of rotten oranges in the queue, we will pop it out and check its neighbors. The timer must be outside of this loop to be accurate. 
            for i in range(curr_rotten_oranges):
                r,c = queue.popleft()
            
                directions = [(-1,0),(1,0),(0,1),(0,-1)]
            
                for direction in directions:
                    # Boundary checking
                    i = direction[0]
                    j = direction[1]
                    new_r = r + i
                    new_c = c + j
                    if new_c < 0 or new_r < 0 or new_r >= rows or new_c >= cols:
                        continue

                    # If this neighbor cell is fresh, it will be rotten
                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2 # Mark it rotten and also visited so that we do not revisit again next time
                        fresh_orange -= 1 # Update fresh orange counter
                        queue.append((new_r,new_c))
                    
        if fresh_orange != 0:
            return -1
        return timer
                    
        
        
        
