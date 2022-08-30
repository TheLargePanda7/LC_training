class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = {0 : 1}
        
        for tar in range(1,target + 1):
            # Initialize a new target range
            dp[tar] = 0
            
            for num in nums:
                # Current root node = target - num
                dp[tar] += dp.get(tar-num,0)
                
        return dp[target]
