class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        """
            Since we need to keep track of the sequence of open and close parenthesis. It is a hint that we need to use stack
            So we can iterate through the string from left to right and keep track of the index of the character that we need to remove
            We push an index of a char to the stack whenever it is an openning parenthesis
            If we detect a closing parenthesis, we must check if our stack is empty. If it is not empty, we found a matching pair. Otherwise, we know that parenthesis are out of sequence and can store its index to remove later
            Eventually, we also need to iterate through the stack again to get indexes of chars to remove because there may be the case that we have extra openning parenthesis.
            Iterate through the original string again and only append the characters if its index are not in the array storing index to remove. 
        
        """
        index_to_remove = []
        stack = []
        res = ""
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) == 0:
                    index_to_remove.append(i)
                else:
                    # Something in there
                    stack.pop(-1)
        
        for j in range(len(stack)):
            index_to_remove.append(stack[j])
        
        
        for k in range(len(s)):
            # k is an index to remove
            if k not in index_to_remove:
                res += s[k]
        return res
            
            
            
                    
                
        
