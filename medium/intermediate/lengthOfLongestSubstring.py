class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Apply sliding windows technique with two pointers
        """
            Assign left and right pointer to be the 0th position initially
            Move the right pointer as long as the characters that we traverse is not in hashmap (not encountering a repeating character yet) to expand the subarray as long as we could
            As soon as a character is in hashmap, this implies that we previously have the same char already and need to move the left pointer to discover another subarray. Assign a current position of repeated character to be its key-value in hash map. This is because we can avoid checking for substrings that we know it has repeating character
            For example:
                        L
                        |
            s =     a   b   c   d   e   a   f   a
                                                |            
                                                R
            map = {
                a: 8,
                b: 2,
                c: 3,
                d: 4,
                e: 5,
                f: 7
            }
            Since we know that substring bcdeafa would contain repeating char, we can move the left pointer to whatever current position + 1 of that repeating character to avoid checking this substring, so in this case L is pointing at "f"
            
        """
        L = 0
        R = 0
        map = {}
        n = len(s)
        res = 0
        
        while R < n:
            if s[R] in map:
                # Adjust the left pointer to be the most current position of repeating character + 1
                # "abba" special case
                # Mistake: L = map[s[R]] -> does not work on "abba"
                # Because the L ptr will be back to the first char "a" which we do not want
                # To fix this, we get the max bwtween current left ptr position and the position of repeating character
                L = max(L,map[s[R]])
                
            map[s[R]] = R + 1
            # Calculate the max len that we discover so far
            res = max(res,R - L + 1)
            R += 1
        return res
                
                
                
                
        
    
        
