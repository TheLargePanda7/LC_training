class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        if target > nums[L]:
            target is on the right subarray
        elif target < nums[L]:
            target is on the left subarray
        
        """
        if not nums:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1
            
        # Apply two pointers technique here
        
        def searchSmallest():
            
            L = 0
            R = len(nums) - 1
            
            # Special case
            if nums[L] < nums[R]:
                # No rotation
                return L
            
            while L <= R:
                mid = (R + L) // 2
                if nums[mid] > nums[mid+1]:
                    return mid+1
                if nums[mid] < nums[mid-1]:
                    return mid

                if nums[mid] > nums[0]:
                    # search left
                    L = mid + 1
                elif nums[mid] < nums[0]:
                    # search right
                    R = mid - 1
                    
                
        i = searchSmallest()
        L = 0
        R = len(nums) - 1
        
        if target == nums[i]:
            return i
        if i == 0:
            L = 0
            R = len(nums) - 1
        else:
            # Adjust pointers because array is rotated
            if target >= nums[0]:
                # Search left
                # if target == nums[0], then there is no way what we are searching for is on the right
                # because nums[0] >> nums[-1] after rotation
                L = 0
                R = i
            elif target < nums[0]:
                L = i
                R = len(nums) - 1
        
        while L <= R:
            mid = (R + L) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                # Search right
                L = mid + 1
            elif target < nums[mid]:
                # Search left
                R = mid - 1
                
            
                
        
        return -1            
            
