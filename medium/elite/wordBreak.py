class Solution(object):
    def wordBreak(self, s, wordDict):
        
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        """
        Initial thought:
        Try out all possible sub-string of string s and check if the sub-stirng is in the dictionary
        Convert the given list to dictionary for O(1) look-up
        
        """
        
        """
        Actual solution (Similar to the above approach, but we add on dynamic programming concept):
        we initialize index i to iterate from 1 to length of string s (this represents the end mark of current substring)
        we also initialize index j to iterate from 1 to i of string s (this represents the beginning of current substring)
        
        By doing so, we basically check all possible substrings that can be formed from string s 
        
        If a substring s1 is in wordDict, we will mark "True" in the dp array with an index of whatever current end mark is.
        For example, s = "leetcode" s1 = s[j=0:i=4] = "leet" and leet is in dictionary
        we mark dp[4] = True to indicate that it is possible to have a valid word up to this point i = 4 (end-index)
        we will also initialize dp[0] to be true since empty string is always a valid string
        dp[len(s)+1] is what we want to return because remember that dp[i] -> True saying that we have valid word to break up to point i
        
        For each possible sub-string, before assigning dp[i] to be true, even the substring satisfies the criteria, we still need to check if dp[j] is true and this is because if it is impossible to break a word at index j, then we do not bother to check the substring from index j to i 
        
        For example:
        
                j                           i
                |                           |
            l   e   e   t   c   o   d   e         wordDict = ["leet","code"]
        
dp =    T   F   F   F   T   ..
        
        First of all, the substring s[j:i] = "eetcode" is not in the dictionary. Second of all, dp[j = 1] = False, which indicates that it was impossible to break any word ending at index j = 1 ("l" is not in dictionary)
        
        Anothey way to explain why we need to check if dp[j] == True because let's say if substring s2 = "code" is in the dictionary, but if substring s1 is not in the dictionary, then combining s1 and s2 together will not make it valid. Think about if we have s = "abcdcode" although code is in dictionary, but abcd is not. Therefore, the whole string "abcdcode" is not possible to be broken down (From the problem requirement,the whole string must be broken down not just a part of it)
        
        """
        # First we need to convert the list to dictionary for constant look-up time
        dict = {}
        for word in wordDict:
            dict[word] = 1
            
                
        
        dp = [False for i in range(len(s)+1)]
        dp[0] = True # Empty string is basically ok
        
        # i starts at index 1 because we already make dp[0] to be true
        for i in range(1,len(s)+1):
            for j in range(i):
                substring = s[j:i] # Remember i is exclusive in index slicing
                # dp[j] is a previous substring and check if it was in the dictionary
                if substring in dict and dp[j] == True:
                        dp[i] = True
                        # Already found a substring that is in dictionary
                        # We do not have to move a pointer j any further
                        break
        print(dp)
        return dp[len(s)]
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
