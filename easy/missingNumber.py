class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Requirements:
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Explanation:
        Given length n of an array, we can sum up all numbers from range of 0 to n
        
        Repeat the same with the given num and keep track of its sum as we iterate
        
        Take the total expected sum (without missing a number) subtracted by the actual sum (the one with missing number) will return the missing number that we are looking for
        
        """
        
        currSum = 0
        total = 0
        for i in range(0,len(nums)+1):
            total += i
            
        for num in nums:
            currSum += num
            
        return total - currSum
