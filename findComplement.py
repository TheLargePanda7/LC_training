class Solution(object):
    
    def helper(self,num,res):
        if num >= 1:
            self.helper(num // 2,res)
        res.append(num % 2)
        
    def BinaryToDecimal(self,num):
        j = 0
        ans = 0
        for i in reversed(range(len(num))):
            if num[i] == "1":
                ans += math.pow(2,j)
            j += 1
        return ans
            
            
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = []
        result = ""
        self.helper(num,res)
        for i in range(1,len(res)):
            if res[i] == 0:
                result += "1"
            else:
                result += "0"
        complement = self.BinaryToDecimal(result)
        return int(complement)
        
        
        
        
        
