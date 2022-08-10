class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(L,R,first):
            n = R
            while L <= R:
                M = (R + L) // 2
                if nums[M] == target:
                    if first:
                        # Search for first occurrence
                        # M - 1 is prev index
                        """
                        Original an if statement such as M == 0 or nums[M] > nums[M-1] also work, but it will rely on second part to return M if the target value is toward the end of the sorted list such as [5,7,7,8,8,10]
                        If we do M == L, when we get down to search space of 2 elements, we can return first occurrence immediately. However, if we do original if statement, we will have to reduce to search space of 1 elements (because M != 0), which is extra iteration.
                        
                        """
                        if M == L or nums[M] > nums[M-1]:
                            # first occurrence detected
                            return M
                        elif nums[M] == nums[M-1]:
                            # element at M is not 1st occurrence
                            # Search right
                            R = M - 1

                    else:
                        # Search for the last occurrence
                        if M == R or nums[M] < nums[M+1]:
                            return M
                        elif nums[M] == nums[M+1]:
                            # element at M is not last occurrence
                            # Search left
                            L = M + 1
                elif nums[M] < target:
                    # Search right
                    L = M + 1
                elif nums[M] > target:
                    # Search left
                    R = M - 1
            
            
            return -1
        
        if len(nums) == 1 and target == nums[0]:
            return [0,0]
        
        first = binary_search(0,len(nums)-1,True)
        
        if first == -1:
            return [-1,-1]
        
        last = binary_search(0,len(nums)-1,False)

        return [first,last]
