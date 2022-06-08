class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        """
        O(log(n)) indicates binary search
        
        Have a left and right pointer and move the pointer according to if the middle element is less or greater than target
        
        target = 5
               L
               |
        arr = [1,3,5,6] 
                     |
                     R
        
        middle = 3 
        
        since middle < 5, we need to look for the right sub array by moving the L pointer to where the middle element is, we have:
        
                   L
                   |
        arr = [1,3,5,6] 
                     |
                     R
                    
        and so on
                 
        """
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            candidate = (right + left) // 2 # Find the middle element and avoid integer overflow at the same time
            
            if nums[candidate] < target:
                # Go to right by adjusting the left pointer
                left = candidate + 1
            elif nums[candidate] > target:
                # Go to left by adjusting the right pointer
                right = candidate - 1
            else:
                # Found it
                return candidate
            
        return left
            
        
                
        
