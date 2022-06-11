class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        curr_prefix = strs[0]
        
        for i in range(1,len(strs)):
            while (strs[i] not in curr_prefix):
                
            while (curr_prefix.index(strs[i])):
        """
        
        # Horizontal Scanning Technique
        
        if len(strs) == 0:
            return ""
        
        curr_prefix = strs[0]
        
        
        for i in range(1,len(strs)):
            # strs[i] = "flow" or "flight"
            # strs[i][:len(curr_prefix)] = "flight" -> "fligh" -> "fli"
            # Each time we reduce a character from our current prefix string until it matches exactly with other strings
            # the statement :len(curr_prefix) of strs[i] is used to truncate characters to the current prefix length
            
            while strs[i][:len(curr_prefix)] != curr_prefix:
                print(strs[i][:len(curr_prefix)])
                curr_prefix = curr_prefix[:len(curr_prefix) -1]
                if len(curr_prefix) == 0:
                    return ""
                
        return curr_prefix
        
