class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
    
        
        """
        cost = [10,15,20]
        
        dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
        
        where can be translated to dp[i-1] is the most optimal cost to reach to step i - 1 adding the cost to pay for using step i-1_th
        
        
        
        For example: 
        
        dp[2] = min(dp[1] + cost[1],dp[0] + cost[0])
        
        Since we are allowed to start either step 0 (10) or step 1 (15), dp[0] and dp[1] are both 0. This is our base case
        
        
        dp[2] = min(0 + 15,0 + 10) = 10
        
        our dp array has one extra element to hold the minimum cost to get to the top (surpassing index len(cost) - 1)
        
        dp[3] = min(dp[2] + cost[2], dp[1] + cost[1]) = min(10 + 20, 0 + 15) = min(30,15) = 15
        
        """
        dp = [0 for i in range(len(cost)+1)] # where dp[i] is a minimum cost to reach step i and need to hold one extra element for the top
        
        for i in range(2,len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            
        return dp[-1]
    
            
        
        
        
