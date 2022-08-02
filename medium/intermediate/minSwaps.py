class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        
        expect_ones = sum(data)
        
        L = 0
        R = 0
        
        currOnes = 0
        maxOnes = 0
        
        while R <= len(data) - 1:
            # Mistake -1: currOnes = sum(data[L:R+1]) - Avoid sum() and subarray computation are expensive
            currOnes += data[R]            
            R += 1
            
            size_of_curr_wind = (R - L)
            # The size of window/subarray exceeds what we want, need to adjust left ptr to keep the size of number ones in original array
            if size_of_curr_wind > expect_ones:
                offset = data[L]
                L += 1
                currOnes -= offset
                
            # Once everything is update (including the size of current window), see if the number ones in this current window is any better than the previous one we computed
            maxOnes = max(maxOnes,currOnes)
            
        return expect_ones - maxOnes
                
            
            
