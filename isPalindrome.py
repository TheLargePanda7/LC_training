class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """
        Iterate through an original string to:
        1. Turn everything back to lowercase letter
        2. Remove non-alphanumeric characters
        3. Remove space
        """
        new_string = ""
        for i in range(len(s)):
            if s[i] == " ":
                continue
            # Check if a character is non-alphanumeric 
            if s[i].isalnum():
                print(s[i])
                if s[i].isupper():
                    # Upper case
                    new_string += s[i].lower()
                else:
                    # Lower case
                    new_string += s[i]
            
        L = 0
        R = len(new_string)
        # Apply two pointers technique to check for Palindrome
        while L < R:
            if new_string[L] == new_string[R-1]:
                L += 1
                R -= 1
            else:
                return False
        return True
                
            
                
            
