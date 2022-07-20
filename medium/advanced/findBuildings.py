class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        
        maxHeight = 0
        
        res = []
        # Traverse from the right to the left and keep track of the maximum height of the building
        # If the current height is taller than maxium height, then it means that current building can see ocean and append to result array
        # Otherwise, it is blocked
        
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > maxHeight:
                maxHeight = heights[i]
                res.append(i)
            elif heights[i] < maxHeight:
                continue
                
        return res[::-1]
                
            
        
                
        
