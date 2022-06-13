class Solution(object):
    def (self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        RequirementscountBinarySubstrings:
        #1 0 as one group and 1 as another group
        #2 Same number of zero and one
        
        We will declare two variables prev and cur to keep track of the groups that we are in
        
        the total binary substring can then be calculated by using this formula res += min(prev,cur)
        
        cur can be calculated by incrementing each time a current character is the same as the previous character. Reset curr to be one whenever we detect curr character is different compared to previous character because we are entering to different group.
        
        prev can be calculated by assigning prev = cur whenever a current character is different compared to the previous character, which signal that we are entering different group either 0 or 1. We take the minimum of prev and cur depending which character has less determine the substring. For example, 001 -> gives us one only because there is only one 1 in the string.
        
        """
        curr = 1 # Keep track of the count of the appearance of the same character (Reset to 1 if we see different char)
        prev = 0 # Keep track of the previous count of the same character as we are about to enter different group and at the same time compare it with the current count and take the minimum of it since the min determines the binary substring (001 -> count = 1 since 1 appears only one)
        res = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                # s[i] != s[i-1]
                res += min(curr,prev)
                prev = curr
                curr = 1
                
        return res + min(curr,prev)
        
                    
