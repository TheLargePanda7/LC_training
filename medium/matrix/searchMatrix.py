class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        O(m * log(n))
        """
        
        def binary_search(r,cols,target):
            curr_arr = matrix[r]
            L = 0
            R = cols - 1
            
            while L <= R:
                M = (R +L) // 2
                if target == curr_arr[M]:
                    return True
                if target > curr_arr[M]:
                    # Search right
                    L = M + 1
                elif target < curr_arr[M]:
                    # Search left
                    R = M - 1
                    
            return False
                
        
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            if binary_search(r,cols,target):
                return True
            
        return False
