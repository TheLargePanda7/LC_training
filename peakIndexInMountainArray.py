class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        """
            Apply Binary Search and two pointers technique:
            
            Suppose we have:
            arr =
                
                L    M  
                [0,1,3,5,2,1]
                            R
        
                arr[M] > arr[M-1], but not > arr[M+1]. This is not a peak
                
                Since arr[M] !> arr[M+1], we know that the peak is somewhere on the right side of the array. In this case,
                we adjust the left pointer to be L = M + 1
                
                Do the opposite if the peak is somewhere on the left side of the arrray
        
        """
        L = 0
        R = len(arr) - 1
        
        while L <= R:
            M = (R + L) // 2
            if arr[M] > arr[M+1] and arr[M] > arr[M-1]:
                # Found the peak
                return M
            else:
                # Need to check where the peak might be
                if arr[M] < arr[M+1]:
                    # The peak is somewhere on the right
                    L = M + 1
                elif arr[M] < arr[M-1]:
                     # The peak is somewhere on the left
                    R = M - 1
        
        
        
        
