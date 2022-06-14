class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
            The idea of this approach is to have two variables to keep track of the recent discovered index of each word
            As soon as the two variables are not -1 (pseudo number we assigned at first), we will compute the distance and take the minimum of the result and previous value we computed.
            
        
        """
        index_w1 = -1
        index_w2 = -1
        currDist = len(wordsDict)
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                index_w1 = i
            elif wordsDict[i] == word2:
                index_w2 = i
            if index_w1 != -1 and index_w2 != -1:
                currDist = min(currDist,abs(index_w1 - index_w2))
                
        return currDist
    
                
        
        
        
        
        
        
        
