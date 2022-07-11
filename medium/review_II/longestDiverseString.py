from heapq import heapify, heappop, heappush
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Notice that the most maximum character occurance always take place first in the result string and then the next maximum character occurance comes second and so on
        For example:
        a = 7 b = 2 c = 1
        Since a is max, then we will first place two characrers of "a" and then only one character of b right after since it is the second max occurence. The reason why we only use one character of the second and third maximum occurance because we want to build the string as long as possible
        Example 2:
        result = aa + b + aa + c + aa + b + a = aabaacaaba
        
        We will use max heap to store the most occurence character and then pop the two elements out from the heap (1st max and 2nd max). 
        We will then compare the two elements together. If they are the same, then we will use one character for each. If they are not (meaning 1s max > 2nd max), we will use two characters of 1st max and one character of 2nd max as shown above in the example
        """
        
        heap = []
        heapify(heap)
        
        # Remember that we construct max heap from min heap by adding a subtrac sign in front of each value
        # If the frequency of a character is 0, we do not care to append to the heap since we will never use it anyway
        if a != 0:
            heappush(heap,(-a,"a"))
        if b != 0:
            heappush(heap,(-b,"b"))
        if c != 0:
            heappush(heap,(-c,"c"))
        
        res = ""
        
        # Since we will pop two elements each time loop iterates, we want to make sure it has a length greater than 1
        while len(heap) > 1:
            # f -> frequency
            # c -> character
            f1,c1 = heappop(heap) # 1st max
            f2,c2 = heappop(heap) # 2nd max
            
            if f1 == f2:
                # Use one character for each
                res += c1 + c2
                # Decrement the counter (it is the opposite since we are using max heap)
                f1 += 1
                f2 += 1
            else:
                # f1 > f2
                # Use two characters for 1st max and only one character for 2nd max
                res += c1 + c1
                res += c2
                
                f1 += 2
                f2 += 1
                
            
            # Important part is to not append any more elements to the heap if the frequency is 0
            if f1 < 0:
                heappush(heap,(f1,c1))
            if f2 < 0:
                heappush(heap,(f2,c2))
                
        print(res)
        # Remember that there may be a case where our heap still has remaining character to add
        """
            We may be wondering that what happens if res = "ccbc" and then remaning character is c. 
            Wouldn't the code below fail? No, it will not because we always pop the first max out and then second max and append characters in that order
            If after the process is done and remaining character is still c, then it must mean that c is the 1st max
            Since c is the 1st max, it will get added first. 
            Remember that the character remaining is always 1st max and get appended before 2nd max. Hence, 2nd max character is always the end of the string and we
            will not have the case such as above to repeat characters consecutively. 
        """
        if heap:
            # Ex: s = "aba" a = 0, b = 1
            # Ex2: s = "aba" a = 0, b = 2
            f,c = heappop(heap)
            if f != 0:
                if f * -1 == 1:
                    res += c
                else:
                    res += c + c
            
        
        return res
            
            
            
            
        
            
                
        
        
        

        
            
            
            
