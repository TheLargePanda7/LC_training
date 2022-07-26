class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        """
        # Naive Approach O(n^3)
        max_length = 0
        
        
        # i : 0 -> 3
        for i in range(len(nums)):
            #j : i+1 -> 3
            for j in range(i+1,len(nums)+1):
                
                subarr = nums[i:j]
                max_element = max(subarr)
                min_element = min(subarr)
                abs_diff = abs(max_element - min_element)
                if abs_diff <= limit:
                    if len(subarr) > max_length:
                        max_length = len(subarr)
        return max_length
        
        """
        # Optimal Solution (Sliding window + two pointers technique)
        maxQueue = deque() # Front contains maximum value
        minQueue = deque() # Front contains minimum value
        maxQueue.append(0)
        minQueue.append(0)
        
        maxLen = 1
        L = 0
        
        for R in range(1,len(nums)):
            # This is to maintain ascending or descending order of both queues
            while minQueue and nums[R] < nums[minQueue[-1]]:
                # Example: nums = [1,3,5] insert 4
                # result nums = [1,3,4]
                minQueue.pop()
            minQueue.append(R)
            
            while maxQueue and nums[R] > nums[maxQueue[-1]]:
                # Example: nums = [5,3,1] and we want to insert 4
                # result nums = [5,4] 
                maxQueue.pop()
            
            maxQueue.append(R)
            
            # Sliding window process explanation:
            # As soon as the maximum absolute exceeds the limit, we need to adjust the left pointer
            # Otherwise, we can keep expanding the subarray by incrementing right pointer to make the longest possible subarray
            while abs(nums[maxQueue[0]]-nums[minQueue[0]]) > limit and minQueue and maxQueue:
                L += 1
                # When we move the left pointer, anything lesser than this index will be irrelavant to our result. Hence, we can go ahead and pop left from both maxQueue and minQueue to update both max and min values as necessary
                # For example, if nums = [10,1,2,4,7,2] and L is pointing at index 1. The value of nums[0] = 10 (index 0 < index L) will no longer be maximum anymore since we do not consider it in our new subarray starting at index L.
                if maxQueue[0] < L:
                    maxQueue.popleft()
                if minQueue[0] < L:
                    minQueue.popleft()
            # If we get to this point, then abs(max-min) < limit, we must check if the length of this new subarray is longer than previous
            maxLen = max(maxLen,R-L+1)
            
        return maxLen
    
            
                
        
        
    
    
        
