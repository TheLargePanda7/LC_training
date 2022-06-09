class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        left_ptr = 0
        right_ptr = len(nums) - 1
        
        while left_ptr <= right_ptr:
            mid_index = (right_ptr + left_ptr) // 2
            
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                # Search left
                right_ptr = mid_index - 1
            else:
                # Search right
                left_ptr = mid_index + 1
        
        return -1
    
                
                
        
