class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        removed_index = []
        substr = ""
        for i in range(len(number)):
            if number[i] == digit:
                removed_index.append(i)
        currMax = -1
        res = ""
        for index in removed_index:
            curr = number
            # Create a substring here
            
            # Before remove character
            before = number[:index]
            
            # After remove character
            after = number[index+1:]
            substr = before + after
                
            currMax = max(currMax,int(substr))
            
        return str(currMax)
