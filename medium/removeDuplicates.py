class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        
        for char in s:
            if len(stack) == 0:
                stack.append((char,1))
            else:
                c,f = stack[-1]
                if char == c:
                    if f + 1 == k:
                        stack.pop()
                    else:
                        # Increase the frequency
                        stack.pop()
                        stack.append((char,1+f))
    
                else:
                    stack.append((char,1))
        # Construct the new string after removal of k adjcent chars        
        res = ""
        for c,f in stack:
            while f:
                res += c
                f -= 1
            
        return res
            
        
        
                    
                        
                
                        
