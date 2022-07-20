class Solution:
    def decodeString(self, s: str) -> str:
        
        # We must realize that ']' indicates that we need to decode the string by popping the digit to multiply with current substring and concatenate it with previous substring (if there is one)
        # When we encounter '[', it indicates that we are done with the current substring and append to the stack because we are about to build another substring (if there is one)
        
        stack = []
        currStr = "" # -> what we would return eventually
        currNum = 0
        
        for char in s:
            if char.isdigit():
                # Calculate the digit given current position
                # currNum * 10 will give us the right starting number. For example, if s = 101[..] and we are at the third digit "0", we will have 10 * 10 = 100, then add 1 to get 101
                currNum = currNum * 10 + int(char)
            elif char == "[":
                # We are done with bulding previous substring and digit, append onto the stack to save it so that we can move on building new one
                stack.append(currStr)
                stack.append(currNum)
                # Reset both variables
                currStr = ""
                currNum = 0
            elif char == "]":
                # Now we need to decode the current substring by multiplying it with frequency k and concatenate with the previous substring stored in the stack (if any)
                freq = stack.pop()
                prev_substr = stack.pop()
                currStr = "".join([currStr]*int(freq))
                currStr = prev_substr + currStr
            else:
                # Just a normal character
                currStr += char
                
        return currStr
            
        
        
                
                    
        
        
