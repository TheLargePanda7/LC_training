from heapq import heapify,heappop,heappush
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        """
        Key point:
        To avoid two adjacent characters are the same, we must give the character with maximum frequency the priority
        
        """
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] =1 
                
        heap = []
        heapify(heap)
        
        for key in dict:
            heappush(heap,(dict[key]* -1,key))
        res = ""
        
        # Explanation: len(heap) > 1 for us to pop two characters at the same time
        while len(heap) > 1:
            # By popping two letters at the same time, we allow to alternate between letters so that we do not push the same letter to the queue over and over again
            """
            For example, if s = aab and only pop one at a time. Next time, we will pop letter a again and append to result string, which does not satisfy the requirement (two adjacent characters are not the same)
            """
            
            f1,c1 = heappop(heap) # Fist max 
            f2,c2 = heappop(heap) # Second max
            # Convert back to actual value since we did it earlier for constructing max heap
            f1 *= -1
            f2 *= -1
            
            # We need to make sure that next time the frequency of each letter is still enough to be added to the result string
            if f1 > 1:
                # Do it again to construct max heap
                heappush(heap,((f1*-1)+1,c1))
            if f2 > 1:
                heappush(heap,((f2*-1)+1,c2))
            # Alternating appending the characters   
            res += c1
            res += c2
        
        # Remember that we also need to take care of the remaining character such as the case when s = "aab"
        # If the frequency of the character is more than 1, then we know it is impossible for us not to repeat the character adjacent at the same time
        if len(heap) == 1:
            f,c = heappop(heap)
            f *= -1
            if f == 1:
                res += c
            else:
                res = ""
        return res
    
            
            
                
                
            
        
        
        
            
        
