class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        mp = defaultdict(int)
        L = 0
        R = 0
        n = len(s)
        size_window = 0
        max_long = 0
        max_frequency_char = 0
        
        # Apply Sliding Window Technique
        while R < n: 
            curr_char = s[R]
            
            # Keep track of frequency of each character
            mp[curr_char] += 1
            
            # Current size of window
            size_window = R - L + 1
            
            # Keep track of character with most appearance in O(1) in time
            max_frequency_char = max(max_frequency_char,mp[curr_char])
            
            # Maximum frequency char - curr window size = characters that can be replaced
            replaceable_char = size_window - max_frequency_char
            
            if replaceable_char <= k:
                max_long = max(max_long,size_window)
            else:
                # Slide the window
                mp[s[L]] -= 1
                L += 1
            R += 1
            
        return max_long
