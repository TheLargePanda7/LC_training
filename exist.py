class Solution(object):
    
    def dfs(self,board,r,c,curr_w):
        
        # If the current word (truncated version) has length of 0, that means we have successfully constructed the path that we want. Return true in such case 
        if len(curr_w) == 0:
            return True
        
        # Check for boundary to make sure we do not exceed the matrix dimension
        # As soon as our current character is not the same as the first character in the board, we do not want to further search this
        if r < 0 or c < 0 or r == len(board) or c == len(board[0]) or board[r][c] != curr_w[0]:
            return False
        
        # Mark visited to avoid searching this coordinate again
        board[r][c] = "visited"
        
        # Traverse to neighbor cells for further investingating
        # Unlike problem 1249, do it one by one instead of all at the same time
        res = [(-1,0),(0,-1),(1,0),(0,1)] # North,West,South, and East
        
        for direction in res:
            row_dir = direction[1]
            col_dir = direction[0]
            # Path found
            if self.dfs(board,r+row_dir,c+col_dir,curr_w[1:]):
                return True
        
        # We marked visited earlier, we have to revert back to original character
        board[r][c] = curr_w[0]
            
            
        
        # If we reach to this point, it means that we already search through the entire array and all possible paths
        return False
        
        
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        """
        Initial thought:
        Iterate through the matrix and check if matrix[i][j] == word[z], if it is, then we perform DFS to further search for neighbor cells. We would also need to pass the index z to dfs method to keep track of the current letter in word for comparison. Remember to create an additional 2-D array with the same size to keep track of the cells that we visited (this will reduces the run-time)
        The approach that we use is very similar to problem number of islands
        
        """
        
        row = len(board)
        col = len(board[0])
        
        for r in range(row):
            for c in range(col):
                if self.dfs(board,r,c,word):
                    return True
                
        return False
            
                
            
        
        
