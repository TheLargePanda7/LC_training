class Solution(object):
    
    def compare(self,short_w,long_w):
        end_index = -1
        for i in range(len(short_w)):
            if short_w[i] == long_w[i]:
                end_index = i
            else:
                break
            
        return end_index
            
                
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # strs[0][L:R] = "f"
        if len(strs) == 1:
            return strs[0]
        
        curr_index = 0
        w1 = strs[0]
        start = True
        
        for i in range(1,len(strs)):
            res = 0
            w2 = strs[i]
            if len(w1) > len(w2):
                res = self.compare(w2,w1)
            else:
                res = self.compare(w1,w2)
            # if res is negative, it means that we found no substr
            
            if res == -1:
                return ""
            
            if res != -1 and start:
                curr_index = res
                start = False
            else:
                curr_index = min(curr_index,res) # Update
                
                
                        
        if curr_index == -1:
            return ""
        
        
        return w1[:curr_index + 1]
            
            
            
