class Solution(object):
    
    def helper(self,s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                return False
        return True
        
    def validPalindrome(self,s):
        
        
            
        """
        :type s: str
        :rtype: bool
        """
        
        """
            Apply two pointers technique to check if a string is a valid palindrome.
            
            Suppose s = "abca"
            
            We have 1 ptr pointing to s[0] = a and another to s[-1] = a
            since they are the same, we move ptrs and now s[1] = b and s[2] = c
            
            since they are different, we can either remove s[1] or s[2] depending which one will gives us palindrome
            
            Write a helper method to check if the candidates. If helper method returns true, we will take that. If both candidates are false, then it means valid palindrome cannot be formed even removing one of the characters
        
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                # Not the same char
                # Remove right ptr
                cand_1 = s[left:right] # bccb [1:5]
                # Remove left ptr
                cand_2 = s[left+1:right+1] # ccbx [2:6]
                return self.helper(cand_1) or self.helper(cand_2)
        return True
                    
                
                
        
            
