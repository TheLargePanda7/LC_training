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
            if size_of_curr_wind > expect_ones:
                offset = data[L]
                L += 1
                currOnes -= offset
            
            maxOnes = max(maxOnes,currOnes)
            
        return expect_ones - maxOnes
                
            
            
