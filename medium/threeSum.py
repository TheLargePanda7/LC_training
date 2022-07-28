class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            x = nums[i]
            # Since array is sorted, if the curr value is the same as previous value. We already found a combination starting at this value
            if i > 0:
                if x == nums[i-1]:
                    continue
            # Now we search for y and z values using two pointers technique
            L = i + 1
            R = n - 1
            
            # The reason L < R because we cannot form a triplet if L == R or y == z
            while L < R:
                y = nums[L]
                z = nums[R]
                currSum = x + y + z
                if currSum > 0:
                    # Sum is too big, need to reduce it by decrementing the R pointer
                    R -= 1
                elif currSum < 0:
                    # Sum is too small, need to increase it by incrementing the L pointer
                    L += 1
                else:
                    # sum == 0
                    res.append([x,y,z])
                    L += 1
                    # Once we found a triplet, we can choose to only move the left pointer
                    # If the sum is still the same after moving the left pointer, we will need to move left pointer again because remember that we cannot have a duplicate triplet
                    # We will continue moving left pointer until we see different value other than the previous as its solution is already computed
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
                    
        return res
            
                
                
                
                  
                    
                        
                        
                    
                    
                    
        
        
            
