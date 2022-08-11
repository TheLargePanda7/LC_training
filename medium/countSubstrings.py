class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        ST -> 7:20
        """
        n = len(s)
        dp = [[False for j in range(n)] for i in range(n)]
        cnt = 0
        # Go through diagonal to fill cells to be True
        for i in range(n):
            dp[i][i] = True
            cnt += 1
        
        # Go through substrings to generate DP cells
        for start in range(n-2,-1,-1):
            for end in range(start+1,n):
                
                # Substring with len of 2 is handled differently
                if end - start == 1:
                    if s[start] == s[end]:
                        dp[start][end] = True
                        cnt += 1
                else:
                    if s[start] == s[end] and dp[start+1][end-1]:
                        dp[start][end] = True
                        cnt +=1
                        
        return cnt
