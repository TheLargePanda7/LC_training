class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        index ends at 0:
        10
        
        index ends at 1:
        10 9
        
        index ends at 2:
        
        [10]
        [10,9]
        
        """
        
        n = len(nums)
        
        dp = [1 for i in range(n)]
        
        for end in range(n):
            for start in range(end+1):
                if nums[end] > nums[start]:
                    dp[end] = max(dp[end],dp[start] + 1)
    
        return max(dp)
    
