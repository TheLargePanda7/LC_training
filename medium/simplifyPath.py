class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # We will split the tokens with a separator of "/" or "//"
        process_path = path.split("/")
        stack = []
        
        # The purpose of this loop is to only add directories into the stack
        for token in process_path:
            if token == '' or token == ".":
                continue
            elif token == "..":
                # Check if we have any directory to pop from the stack
                # If not, it means that there is not previous directory to go back to
                if len(stack) >= 1:
                    #print(stack)
                    stack.pop()
            else:
                # Directory
                stack.append(token)
                
        # When we only have root directory, the stack is emty
        if not stack:
            return "/"
        
        # Begin building our canonical path
        # Each token in stack is a directory
        canonical_path = ""
        for i in range(len(stack)):
            token = stack[i]
            # Remember there is always a / in front of each directory
            canonical_path += "/" + token
        return canonical_path
                
                
                    
            
                    
                
            
