class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        # Transpose the array in-place
        for i in range(0,n):
            for j in range(i,n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        # Swap values in column i with n-1-i
        for i in range(n):
            for j in range(n):
                new_index = n-1-i
                if new_index < i:
                    break
                matrix[j][i],matrix[j][new_index] = matrix[j][new_index],matrix[j][i]
