class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        """
            Intuition:
            Since the array may be rotated, we need to compare the target with the 0th element (remember that 0th-element is always greater than the last element after rotation)
            From there, we can tell where to look for (either left or right)
            However, there is no divider (like if we look the left, when do we stop looking for the left or in other words, where the left ends?)
            Hence, we need the index of smallest element and use it as divider of left and right subarrays to look for.
        """
        # Edge case
        if not nums:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        if len(nums) == 1 and nums[0] != target:
            return -1
        
        
        # Binary Search using 2 ptrs technique
        index_smallest = 0
        
        # First find the index of smallest element using binary search
        def findSmallestIndex(nums):
            L = 0
            R = len(nums) - 1
            
            if nums[L] < nums[R]:
                # No rotation
                return 0
            
            while L <= R:
                # Middle index
                M = (R + L) // 2
                
                # Checking if nums[M] is an inflection point
                if nums[M] > nums[M+1]:
                    return M+1
                elif nums[M] < nums[M-1]:
                    return M
                # [2,3,4,5,6,7,0,1]
                # Compare with 0th element to find inflection point
                if nums[M] > nums[0]:
                    # Search right
                    L = M + 1
                elif nums[M] < nums[0]:
                    # Search left
                    R = M - 1
                
                
        index_smallest = findSmallestIndex(nums)
        
        # Find the smallest element is target, return it
        if target == nums[index_smallest]:
            return index_smallest
        # Special case -> no rotation
        if index_smallest == 0:
            L = 0
            R = len(nums) - 1
        else:
            # Compare target with 0th-index element in array
            # If the target is greater than 0th-index element, we search left of index of smallest element
            # Otherwise, we search right of index of smallest element
            if target >= nums[0]:
                # divider = smallest element
                # Search left of divider (inclusive)
                # if target == nums[0], then there is no way what we are searching for is on the right
                L = 0
                R = index_smallest
            elif target < nums[0]:
                # Search right of divider (inclusive)
                L = index_smallest
                R = len(nums) - 1
                

        # After getting specific space that we need to search, just perform another binary search to get target
        while L <= R:
            M = (R + L) // 2
            if nums[M] == target:
                return M
            if target > nums[M]:
                # Search right
                L = M + 1
            else:
                # Search left
                R = M - 1
                
        return -1
        
        
            
            
        
        
        
            
            
        
        
        
        
        
        
        
