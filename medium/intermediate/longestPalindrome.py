class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        """
        s = "babad"
        dp[0][0] = b
        dp[0][1] = ca
        dp[0][2] = cab
        dp[1][1] = a
        dp[1][2] = ab
        and so on
        """
        # Declare n x n matrix where each cell represents a certain substring
        dp = [ [False for j in range(len(s))] for i in range(len(s)) ]
        
        max_length = 0
        res = ""
        # Initialize the base case where i == j -> a character and a single character is palindrome
        # Diagonal direction will all be True
        for i in range(n):
            dp[i][i] = True 
            res = s[i]
            max_length = len(res)
                    
        
        # i: start index
        # j: end index
        
        # Iterating from bottom to top in the matrix
        for i in range(n-1,-1,-1):
            # Iterating from left to top (but only the portion above diagonal)
            for j in range(i+1,n):
                # Check if the outermost character (both left and right) equal each other
                if s[i] == s[j]:
                    # Need to check if the length of substring is exactly 2
                    # Also check if its inner substring is also palindrome before (..aba..)
                    #if j - i == 1:
                        #print(len(s[i:j+1]))
                    if j - i == 1 or dp[i+1][j-1]:
                        # If inner substring is palindrome (example: aba)
                        # and outer characters are the same (example: z aba z)
                        # then this must also be a palindrome (zabaz)
                        dp[i][j] = True
                        if len(s[i:j+1]) > max_length:
                            
                            # Update the length of longest palindromic substring so far
                            res = s[i:j+1]
                            max_length = len(res)
                            
                        
        return res
        
                
