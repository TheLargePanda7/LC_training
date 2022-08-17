class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        # Start 6:13
        L = 0
        R = 0
        n = len(cardPoints)
        maxPoint = 0
        maxSize = n - k # Maxium width of window we can have
        currSize = 0
        totalSum = sum(cardPoints)
        currSum = 0
        
        while R < n:
            currSum += cardPoints[R]
            currSize = (R - L) + 1
            if currSize > maxSize:
                currSum -= cardPoints[L]
                L += 1
                
            if (R - L) + 1 == maxSize:
                maxPoint = max(maxPoint,totalSum - currSum)
            
            R += 1
        return maxPoint
