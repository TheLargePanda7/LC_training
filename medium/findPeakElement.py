class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Start tiime: 6:12
        
        # Base cases
        if len(nums) == 1:
            return 0
        n = len(nums)
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[n-2]:
            return n-1
        
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            
            M = (R + L) // 2
            # Case 1
            if nums[M] > nums[M-1] and nums[M] > nums[M+1]:
                return M
            
            # Case 2
            if nums[M] < nums[M+1] and nums[M] > nums[M-1]:
                L = M
            
            # Case 3
            if nums[M] > nums[M+1] and nums[M] < nums[M-1]:
                R = M
            
            # Case 4
            if nums[M] < nums[M+1] and nums[M] < nums[M-1]:
                R = M
            
            
        return -1
