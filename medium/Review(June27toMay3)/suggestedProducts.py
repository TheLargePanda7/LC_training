from string import ascii_lowercase

class TrieNode(object):
    def __init__(self):
        self.children = [None for i in range(26)]
        self.IsitWord = False
        self.word = None
        
class Solution(object):
    
    def dfs(self,curr,prefix,subarray):
        
	    
        if len(subarray) >= 3:
            return
        if curr.IsitWord:
            subarray.append(prefix) # Two ways to go about this: we can either do subarray.append(curr.word) or the one that we have now
            
        # Remember that if the current node has more than 3 childrens, then we will priotize returning the words lexicographically
        # So we want to iterate from a to z to have that priority property
        for c in ascii_lowercase:
            if curr.children[ord(c) - ord('a')] != None:
                # Recursively traverse the Trie to get the next character in line 
                self.dfs(curr.children[ord(c) - ord('a')],prefix + c,subarray)
                
    
            
    def getLastCharInPrefix(self,prefix,root):
        curr = root
        sub_array = []
        
        # Traverse Trie to get the ptr to the last char of prefix
        for char in prefix:
            if curr.children[ord(char) - ord('a')] != None:
                curr = curr.children[ord(char) - ord('a')] # Adjust pointer
            else:
                return sub_array
            
                
        
        # Once we get here, curr is a pointer to the last character of prefix. We need to call another method to keep traversing the Trie to get the actual words
        self.dfs(curr,prefix,sub_array)
        return sub_array
        
        
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        root = TrieNode()
        
        
        # build our Trie nodes here
        for product in products:
            # Each time, we reset the curr pointer to be at root because we want to start from the begining to check if the character is already in the trie
            curr = root 
            
            for char in product:
                if curr.children[ord(char) - ord('a')] == None:
                    # Node for character i does not exist, need to create a new one
                    newNode = TrieNode()
                    curr.children[ord(char) - ord('a')] = newNode
                curr = curr.children[ord(char) - ord('a')] # Update current word so that we can continously build our trie with the rest of characters
                
            # At this point, curr is not a root node, but a leaf node that lead to a complete word        
            curr.IsitWord = True
            curr.word = char # Error: this should be "curr.word = product"
            
        res = []
        prefix = ""
        for char in searchWord:
            """
		    word = mouse
		    prefix = m, mo, mou,mous,mouse
		    """
            prefix += char
            
            # Given a prefix, now traverse the Trie to get a pointer to the node of last char in prefix
            # The method will also return an array of words that starting with the current prefix
            res.append(self.getLastCharInPrefix(prefix,root))
            
        return res

        
        
