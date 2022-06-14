class Solution(object):
    
    def compareDict(self,superset,subset,wordCnt):
        count = 0
        for key in subset:
            if key in superset:
                if superset[key] >= subset[key]:
                    count += subset[key]
            
        if wordCnt == count:
            return True
        else:
            return False
                
                    
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        dict = {}
        for char in chars:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        
        res = 0
        for i in range(len(words)):
            sub_set = {}
            curr_count = 0
            for char in words[i]:
                #print(char)
                curr_count+=1
                if char not in sub_set:
                    sub_set[char] = 1
                else:
                    sub_set[char] += 1
                    
            if self.compareDict(dict,sub_set,curr_count):
                res += curr_count
                
            

                
        return res
            
        
        
        
        
