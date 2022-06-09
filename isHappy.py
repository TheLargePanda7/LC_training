class Solution(object):
    
    
    def getNextVal(self,n):
        curr_numb = str(n)
        curr_val = 0
        for i in range(len(curr_numb)):
            curr_val += (int(curr_numb[i]) * int(curr_numb[i]))
        return curr_val
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
            Idea:
            To detect any cycle, which there could potentially be, we will apply Floyd's Cycle-Finding Algorithm
            The idea is that we will have two runners, rabbit and turtle, where rabbit runs twice as fast as turtle. 
            If there is indeed a cycle, both will eventually meet up each other
            To avoid writing extra code, we will have a helper method to help us get the next number of n.
            The loop continues as long as the rabbit does not reach the destination (meaning finding the happy number) or the rabbit does not meet the turtle (meaning infinity loop)
        
        """
        
        turtle = n
        rabbit = self.getNextVal(n)
        while rabbit != turtle and rabbit != 1:
            turtle = self.getNextVal(turtle)
            rabbit = self.getNextVal(self.getNextVal(rabbit))
        if rabbit == 1:
            return True
        else:
            return False
            
                
                
                
            
        
