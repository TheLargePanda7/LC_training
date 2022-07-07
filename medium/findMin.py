class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        start time 5:45
        
        nums = [0,1,2,3,4,5,6,7]
        
        nums = [1,2,3,4,5,6,7,0] -> rotate 1
        
        nums = [2,3,4,5,6,7,0,1] -> rotate 2
        
        nums = [3,4,5,6,7,0,1,2] -> rotate 3
        
        nums = [4,5,6,7,0,1,2,3] -> rotate 4
        
        continue until we rotate n times
        
        Goal: 
        Find minimum element of the rotated array
        
        Requirement: log(n)
        
        
        
        """
        if len(nums) == 1:
            return nums[0]
        L = 0
        R = len(nums) - 1
        
        # Perfect order without rotation
        if nums[L] < nums[R]:
            return nums[0]
        
        
        while L <= R:
            
            mid = (L + R) // 2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            
            if nums[mid] < nums[0]:
                # Minimum value is on the left side
                R = mid - 1
            elif nums[mid] > nums[0]:
                # Minimum value is on the right side
                L = mid + 1
        
    
                
                
        
