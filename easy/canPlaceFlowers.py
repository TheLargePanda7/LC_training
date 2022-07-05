class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        
        for i in range(len(flowerbed)):
            
            if flowerbed[i] == 0:
                # Edge case
                if i == 0 or flowerbed[i-1] == 0:
                    left = True
                else:
                    left = False
                
                if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                    right = True
                else:
                    right = False
                
                if left and right:
                    flowerbed[i] = 1
                    cnt += 1
                
                    
                    
                    
        if cnt >= n:
            return True
        return False
        
        
                
                    
                    
