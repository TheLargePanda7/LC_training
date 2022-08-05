class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Sliding Window Technique using 2 poitners
        L = 0
        R = 0
        n = len(s)
        mp = {}
        maxSub = 0
        maxSameCharsInWindow = 0
        
        while R < n:
            if s[R] not in mp:
                mp[s[R]] = 1
            elif s[R] in mp:
                mp[s[R]] += 1
            
            size_of_window = R - L + 1
            
            # the current counter in mp will always win since that is the most recent updated frequency of max char
            # However, using mp[max(mp, key = mp.get)] is O(n)
            # To avoid this, we can just have a variable to keep track of current max char. So it will be O(1)
            maxSameCharsInWindow = max(maxSameCharsInWindow,mp[s[R]])
            replaceable_char = size_of_window - maxSameCharsInWindow
            
            
            if replaceable_char <= k:
                maxSub = max(maxSub,size_of_window)
            elif replaceable_char > k:
                # Not possible to replace
                # Update frequency of skipped character
                mp[s[L]] -= 1
                L += 1
                
            R += 1
                
        return maxSub
            
            
                        
            
            
        
        
        
