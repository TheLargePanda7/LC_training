class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,3,4]
        ans = [24,12,8,6]
        Run-time Requirement: O(n)
        
        General Case:
        nums = [2,3,4] totalProd = 24
        ans = [12,8,6] -> ans[i] = totalProd / nums[i]
        
        Edge Case:
        #1
        nums = [-1,1,-0,-3,3] totalProd = 0, temp = 9 
        if nums[i] == 0:
            ans[i] = temp
        #2 
        nums = [0,1,0,-3,3] totalProd = 0, temp = -9
        both nums[0] and nums[2] are 0:
            ans[0] and ans[2] = temp
        
        Time: O(n)
        Space: O(1) -> answer array does not count
        
        """
        
        n = len(nums)
        ans = [0 for i in range(n)]
        totalProd = 1
        temp = 1 # We need this variable to keep track of the edge case where we have exactly one zero in array
        cnt = 0
        # Need to count the number of zeroes
        # If we have more than one zero, it is impossible to make a product non-zero numbers in the array
        for num in nums:
            if num == 0:
                cnt += 1
                
        if cnt == len(nums):
            return nums
        elif cnt > 1:
            return ans
        
        for num in nums:
            if num != 0:
                temp *= num
            totalProd *= num
        print(totalProd)
        
        
        for i in range(n):
            if nums[i] == 0:
                ans[i] = temp
            else:
                ans[i] = int(totalProd / nums[i])
        return ans
