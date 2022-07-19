class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        n = len(nums)
        
        def backtrack(index,curr):
            if index >= len(nums):
                # Remember that curr is a pointer to 0th element of array in memory space. Because we are going to modify it via backtracking, the pointer that we append to res array will also be changed, which we do not want that
                # To fix this issue, use index slicing to create an array in a new memory space and copy all elements from the original to the new array
                new_mem_space = curr[:]
                res.append(new_mem_space)
                return
            
            # We have two different decisions to make for each element
            # 1. include nums[index]
            # 2. NOT to include nums[index]
            
            # Decsion 1
            curr.append(nums[index])
            # Carry the decision that we made for current level to next level with curr
            backtrack(index+1,curr)
            
            # Bactrack to choose decision 2
            curr.pop()
            
            # Decsion 2. Again carry through the decision that we made (not to include nums[index]) with curr to the next level of decision tree
            backtrack(index+1,curr)
            
            
            
        
        # Start with 0th element
        curr = []
        backtrack(0,curr)
            
        return res
