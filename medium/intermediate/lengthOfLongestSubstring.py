lass Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = 0
        R = 0
        
        # Index = character
        # Value = index of that character (where it is most recently seen)
        mp = {}
        longestSub = 0
        
        while R < len(s):
            if s[R] in mp:
                # Get the index of this repeated character (previous seen)
                prev = mp[s[R]]
                
                # Because this character is repeated somewhere before, we will adjust left ptr to be 1 + where it is so that we can avoid computation
                # However, keep in mind that we could have seen the repeated character way before current index L as it happens when we have more than one repeated character such as abba where we already adjusted L ptr to be most recent b, but then encounter "a" lastly, which made us to adjust L ptr to point to first "a" (we do not want this).
                # Mistake: L = map[s[R]] -> does not work on "abba"
                # Hence, we need to take a max of the highest current index of L (think about s = "abba")
                L = max(prev,L)
                
            # Regardless if current char is in map or not, we still need to (1) append to map or (2) update this curr char most recently seen index
            # Update the most recently seen index of this repeated character
            mp[s[R]] = R + 1
            longestSub = max(longestSub,R-L+1)
            R += 1
            
        return longestSub
