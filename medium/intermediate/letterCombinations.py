class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Apply Backtracking Algorithm
        
        """
        # Edge case
        if len(digits) == 0:
            return []
        
        res = []
        phonebook = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        
        def backtrack(path,index,res,digits,phonebook):
            # Base case: if our current path construction has the same length as length of digits, we reach the leaf node in decision tree and complete one of the possible combinations.
            if len(path) == len(digits):
                # We reach the leaf node of decision tree, now append one of the possible combination strings into the array
                possible_combinations = "".join(path) #Path is an array, we need to convert to string
                res.append(possible_combinations)
                return
            
            # Get possible letters given current number
            letters = phonebook[digits[index]]
            
            for letter in letters:
                #print(digits[index],letter)
                path.append(letter)
                # Recursively traverse to the next level of the decision tree
                backtrack(path,index+1,res,digits,phonebook)
                # we backtrack to move onto the next possible combinations using the given path or we can see to move to different route in decision tree
                path.pop()
                
                
            
            
        backtrack([],0,res,digits,phonebook)
        return res
        
        
