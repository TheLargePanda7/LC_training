class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Start: 7:05
        
        
        rows = m
        cols = n
        dp = [[0 for c in range(cols) ] for r in range(rows)]
        dp[0][0] = 1
        # Base case
        for c in range(1, cols):
            dp[0][c] = 1
        for r in range(1, rows):
            dp[r][0] = 1
        
        # DP Formation
        for r in range(1, rows):
            for c in range(1,cols):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        return dp[-1][-1]
        
        
        
        """
        DFS Solution (TLE - because we recomputed paths)
        unique_cnt = 0
        def dfs(r,c,rows,cols):
            nonlocal unique_cnt
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if r == rows - 1 and c == cols - 1:
                unique_cnt += 1
                
            # Go to right
            dfs(r,c+1,rows,cols)
            
            # Go to bototm
            dfs(r+1,c,rows,cols)
            
            return
            
        
        
        
        dfs(0,0,rows,cols)
        #for r in range(rows):
        #    for c in range(cols):
        #        dfs(r,c,rows,cols)
        return unique_cnt
        
        
        """
