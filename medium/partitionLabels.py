class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        mp = {}
        
        for i in range(len(s)):
            mp[s[i]] = i
        res = []
        index_end = 0
        size = 0
        
        for i in range(len(s)):
            char = s[i]
            index_last = mp[char]
            size += 1
            # Order matters
            if index_last > index_end:
                index_end = index_last
            if i == index_end:
                res.append(size)
                size = 0
            
            
        return res
