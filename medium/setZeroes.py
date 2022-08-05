class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0]) 
        
        SetRowZero_Zero = False
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    
                    # Mark it as a flag
                    matrix[0][c] = 0 # Signal to mark every single row in c-th col to be zero (Vertical)
                    
                    # Special case
                    # Prevent conflict from having a 0 element at r = 0 and c = 0 with marking entire 0th col to be zero
                    if r > 0:
                        matrix[r][0] = 0 # Signal to mark every single col in c-th row to be zero (Horizontal)
                    else:
                        SetRowZero_Zero = True
        
        # Begin modifying cells
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    # Signal to mark the entire row or col to be zero
                    matrix[r][c] = 0
                    
        # Denotes that this cell is 0 not because of modification.
        # Therefore all rows in col 0th must be marked zero
        # Remember the for loop above only takes care of inner matrix (the outer portion is used for the flag)
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # Denotes that we need to mark all cols in row 0th to be 0
        if SetRowZero_Zero:
            for c in range(cols):
                matrix[0][c] = 0

                        
        
