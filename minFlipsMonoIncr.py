class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
            Observation I:
            The very first "1" in the string s is the beginning of the window of the group that we need to take care of
            For example:
            s = "001010"
            At index = 2 is where the first 1 appears. So we would look from index = 2 to the end of the string because we will not need to flip anything before index = 2
            
            Observation II:
            To produce minimum operation of flip
            If the number of zeroes is greater than the number of ones, then we flip ones
            If the number of ones is greater than the number of zeroes, then we flip zeroes
            Otherwise, it does not matter what we choose
            
            Edge cases (Follow up):
            What happens if all zeroes or all ones?
            
            Special case (where my initial algorithm fails):
            0101100011
            
            Problem: 
            We assume that we need to flip all ones or all zeroes in the window (subarray that starts at index i where "1" is first found). However, we do not need to
        """
        
        """
        Correct and optmized solution:
        Declare two variables flipOne and flipZero
        flipOne: counter of flip operation from 1 to 0
        flipZero: counter of flip operation from 0 to 1
        Take the minimum of the two and assign it to flipZero (this is because keep track of flipping 1 to 0 is more important since we want to maintain the increasing order of binary - to prevent the case such that we cannot flip 1 to 0 in the prior index due to more zeros that we encounter along the way)
        """
        
        flipZero = 0
        flipOne = 0
        
        for numb in s:
            if numb == "1":
                flipOne += 1
            else:
                flipZero += 1
                
            # DP - use a previous optimal solution to compute for the current optimal solution
            flipZero = min(flipZero,flipOne)
            
            
        return flipZero
    
    
                
        
        
    
            
            
            
            
                
        
        
        
        
        
