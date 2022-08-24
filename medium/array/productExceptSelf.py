class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time start: 6:53
        # Requirements: O(n) in time and O(1) in space -> single loop
        """
        1: [2,3,4]
        2: [1,3,4]
        3: [1,2,4]
        4: [1,2,3]
        
        """
        n = len(nums)
        var_R = 1 # Keep track of pre-computed product of all elements to the right of current index i
        res = [0 for i in range(n)]
        res[0] = 1
        
        # Build left array
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        
        # Build right array using var_R and also produce the answer using L array in res array
        for i in range(n-1,-1,-1):
            res[i] = res[i] * var_R
            var_R *= nums[i] # Compute the product of elements to the right of current element (stacked as we traverse)
            
        return res
