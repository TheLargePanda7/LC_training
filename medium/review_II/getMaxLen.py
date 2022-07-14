class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        The goal is to find the maximum possible length of subarray in the given array such that the product of all of its elements are positive
        
        The important observation is:
        negative * positive = negative
        negative * negative = positive
        positive * positive = positive
        0 * anything = 0
        
        if we keep encountering a positive number, the length of subarray will keep increasing
        if we keep encountering a negative number, the result will alternate
        
        -> Hence, we must keep track of maximum and minimum product values 
        
        """
        pos = [0 for i in range(len(nums))]
        
        neg = [0 for i in range(len(nums))]
        
        # Base case
        if nums[0] > 0:
            pos[0] = 1
            neg[0] = 0
        elif nums[0] < 0:
            pos[0] = 0
            neg[0] = 1
            
        # Dynamic Programming Algorithms
        for i in range(1,len(nums)):
            if nums[i] > 0:
                if pos[i-1] != 0:
                    pos[i] = 1 + pos[i-1] # (+) * (+) = (+)
                else:
                    pos[i] = 1 # Previous value is 0, let's separate the subarray
                
                if neg[i-1] != 0:
                    neg[i] = 1 + neg[i-1] # (+) * (-) = (-)
                else:
                    neg[i] = 0 # No negative subarray can be constructed so far
                
            elif nums[i] < 0:
                # There exists a positive product with length n at previous index i
                if pos[i-1] != 0:
                    neg[i] = 1 + pos[i-1] # (+) * (-) = (-) -> multiplying neg number with positive product subarray will expand negative product subarray
                else:
                    # pos[i-1] == 0 (there exists no positive product subarray at the previous index)
                    """
                    For example:
                        [-1,-2]
                    pos: 0  2
                    neg: 1  1
                    """
                    neg[i] = 1 # A new subarray containing negative product is discovered or continue negative product subarray with same length as shown above
                
                # There exists a negative product with length n at previous index i
                if neg[i-1] != 0:
                    pos[i] = neg[i-1] + 1 # (-) * (-) = (+) -> multiplying neg number with negative product subarray will expand positive product subarray
                else:
                    pos[i] = 0 # Cut-off the current element from the subaray since it is negative
                    
                    
        return max(pos) # pos contains all possible length of subarray including subarrays that had been cut-off by 0. Return the max length
                    
        
        
        
        
        
        
        
