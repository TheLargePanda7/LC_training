class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Apply Binary Seach TWO times to find the beginning and ending index
        def binary_search(nums,target,first_index):
            L = 0
            R = len(nums) - 1
            
            while L <= R:
                M = (R + L) // 2
                if nums[M] == target:
                    if first_index:
                         # Search for start index    
                        if M == L or nums[M] > nums[M-1]:
                            return M

                        # nums[M] is not first occurence
                        # Must be located on the left half of M
                        R = M - 1
                    else:
                        # Search for end_index
                        if M == R or nums[M] < nums[M+1]:
                            return M
                        # nums[M] is not last occurence
                        # Must be located on the right half of M
                        L = M + 1
                elif nums[M] < target:
                    # Target may be on the right of mid
                    L = M + 1
                elif nums[M] > target:
                    # Target may be on the left of mid
                    R = M - 1
            return -1
        
        start_index = binary_search(nums,target,True)
        if start_index == -1:
            return [-1,-1]
        
        end_index = binary_search(nums,target,False)
        
        return [start_index,end_index]
