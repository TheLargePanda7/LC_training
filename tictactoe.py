class Solution(object):
    
        
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        
        """
        Splits the moves between two players:
        A = [(0,0),(1,1),(2,2)]
        B = [(2,0),(2,1)]
        
        Iterate through 3x3 grid and mark the move from player based on 2 arrays above:
        [
            A,'',''
            '',A,''
            B,B,''
        ]
        
        Iterate through 3x3 grid again to see if any row, column, or diagonal are the same
        
        """
        
        A = []
        B = []
        
        
        for i in range(len(moves)):
            if i % 2 == 0:
                # Even -> A
                A.append(moves[i])
            else:
                # Odd -> B
                B.append(moves[i])
        
        
        rows, cols = (3, 3)
        grid = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(3):
            for j in range(3):
                if [i,j] in A:
                    grid[i][j] = 'A'
                elif [i,j] in B:
                    grid[i][j] = 'B'
                else:
                    grid[i][j] = 'Empty'
        
        A_cnt = 0
        B_cnt = 0
        empty_cnt = 0
        
        print(grid)
        #Row first
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'A':
                    A_cnt += 1
                elif grid[i][j] == 'B':
                    B_cnt += 1
                else:
                    empty_cnt += 1
            if A_cnt == 3:
                return "A"
            elif B_cnt == 3:
                return "B"
            # Reset before moving on next row
            A_cnt = 0
            B_cnt = 0
            
        # A = 1, B = 2, empty_cnt = 4
        print(A_cnt)
        print(B_cnt)
        
        A_cnt = 0
        B_cnt = 0
        
        # Check column 
        for j in range(3):
            for i in range(3):
                if grid[i][j] == 'A':
                    A_cnt+= 1
                elif grid[i][j] == 'B':
                    B_cnt+= 1
                else:
                    continue
            if A_cnt == 3:
                return "A"
            elif B_cnt == 3:
                return "B"
            # Reset before moving on next column
            A_cnt = 0
            B_cnt = 0
        
        A_cnt = 0
        B_cnt = 0
        
        
        # Check diagonal #1
        if grid[0][0] == 'A':
            A_cnt+= 1
        if grid[1][1] == 'A':
            A_cnt+= 1
        if grid[2][2] == 'A':
            A_cnt+= 1
            
        if grid[0][0] == 'B':
             B_cnt+= 1
        if grid[1][1] == 'B':
             B_cnt+= 1
        if grid[2][2] == 'B':
            B_cnt+= 1
            
        if A_cnt == 3:
            return 'A'
        elif B_cnt == 3:
            return 'B'
        A_cnt = 0
        B_cnt = 0
            
         # Check diagonal #2
        if grid[0][2] == 'A':
            A_cnt+= 1
        if grid[1][1] == 'A':
            A_cnt+= 1
        if grid[2][0] == 'A':
            A_cnt+= 1
            
        if grid[0][2] == 'B':
             B_cnt+= 1
        if grid[1][1] == 'B':
             B_cnt+= 1
        if grid[2][0] == 'B':
            B_cnt+= 1
            
            
        if A_cnt == 3:
            return 'A'
        elif B_cnt == 3:
            return 'B'
        elif empty_cnt != 0:
            return "Pending"
        else:
            return "Draw"
            
  
                 
