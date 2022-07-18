class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Two pointers technique + greedy choice to move pointer
        L = 0
        R = len(height) - 1
        maxWater = 0
        while L < R:
            width = R - L
            maxWater = max(maxWater,min(height[L],height[R]) * width)
            
            
            # Adjust pointers (choosing a higher height over shorter)
            if height[L] < height[R]:
                L += 1
            elif height[L] > height[R]:
                R -= 1
            else:
                # If they are the same, it does not matter
                L += 1
                R -= 1
            
            
            
            
        return maxWater
                
            
