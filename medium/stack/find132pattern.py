class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Start time: 7:13
        """
        [-1,3,2,0]
        [-1,0,2,3]
        """
        """
        n = len(nums)
        # Navie solution - TLE O(n^3)
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if nums[i] < nums[k] and nums[k] < nums[j]:
                        return True
                    
        return False
        """
        
        # Monotonic Stack (Decreasing order)
        stack = []
        minVal = nums[0]
        n = len(nums)
        for i in range(1,n):
            # Maintain descending order 
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            
            if len(stack) > 0 and nums[i] > stack[-1][1]:
                return True
            
            stack.append((nums[i],minVal))
            
            minVal = min(minVal,nums[i])
            
            
        return False
