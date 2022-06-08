import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Without O(1) approach:
        container = {}
        
        for i in range(len(nums)):
            
            if nums[i] not in container:
                container[nums[i]] = 1
            else:
                container[nums[i]] += 1
                
        print(container)
        cur_max = 0
        res_key = 0
        for key in container:
            if container[key] > cur_max:
                cur_max = container[key]
                res_key = key
                
                
        return res_key
        """
        
    
        """
        With O(1) approach
        We must sort the array in ascending order. Notice that the question gives us the big hint that the majority element is an element that appears more than floor(n/2) times. Given this information, if we sort it and return the middle element, the middle element must always be an element that has frequency at least n/2 times because of the nature of it. 
        arr = |---major---|---not-major----|
        or
        arr = |---not-major----|---major---|
        """
        nums.sort()
        middle_index = int(math.floor(len(nums) / 2))
        
        return nums[middle_index]
        
                
            
                
            
        
        
