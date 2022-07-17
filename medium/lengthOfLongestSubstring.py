class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        
        map = {}
        # Sliding window + hashmap technique
        L = 0
        R = 0
        maxLen = 0
        # Edge case: no duplicate letter
        dup = False
        for char in s:
            if char in map:
                # Duplicate detected
                map = {}
                dup = True
                break
            else:
                map[char] = 1
        if dup == False:
            return len(s)
        
        
        while R <= len(s) - 1:
            if s[R] not in map:
                map[s[R]] = 1
                # Continue extending the width of window (increasing the length of substring)
                R += 1
                # Handling edge case
                if R > len(s) - 1:
                    maxLen = max(maxLen,len(map))
                    
            else:
                maxLen = max(maxLen,len(map))
                
                # Readjust pointers
                L += 1
                R = L
                # Delete all elements in map to start over
                map = {}
        
        
        return maxLen
                
                
                
                
                
        
