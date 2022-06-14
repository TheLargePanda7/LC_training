class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Check for empty string
        if len(needle) == 0:
            return 0
        
        if len(needle) == len(haystack):
            if haystack == needle:
                return 0
        
        for front in range(len(haystack)):
            if haystack[front] == needle[0]:
                if haystack[front:front+len(needle)] == needle:
                    return front
        return -1
                
