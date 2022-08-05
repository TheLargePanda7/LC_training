class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        L = 0
        R = 0
        mp = {}
        longestSub = 0
        
        while R < n:
            #print(L,R,mp)
            if s[R] not in mp:
                mp[s[R]] = 1
                
                # There are more distinct characters in hashmap than k
                if len(mp) > k:

                    # Update map
                    mp[s[L]] -= 1
                    #print("hello",mp[s[L]])
                    if mp[s[L]] == 0:
                        del mp[s[L]]    
                    # Need to change L ptr
                    L += 1
                    
                    
                else:
                    # Only compute substring if we satisfy the requirement of k
                    longestSub = max(longestSub,R-L+1)
                    
            elif s[R] in mp:
                mp[s[R]] += 1
                if len(mp) > k:
                    mp[s[L]] -= 1
                    if mp[s[L]] == 0:
                        del mp[s[L]]    
                    # Need to change L ptr
                    L += 1
                else:
                    # We are safe to advance since we do not add extra element into map
                    longestSub = max(longestSub,R-L+1)
            
            R += 1
            
        return longestSub
        
