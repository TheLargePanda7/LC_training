class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = [None for i in range(26)]
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if curr.children[ord(char)-ord('a')] == None:
                # Declare a new node
                new_node = TrieNode()
                curr.children[ord(char)-ord('a')] = new_node
            curr = curr.children[ord(char)-ord('a')] # Move on to next node
        curr.word = True
            
            
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        # Traverse through the Trie to search for word
        curr = self.root
        for char in word:
            if curr.children[ord(char)-ord('a')] != None:
                curr = curr.children[ord(char)-ord('a')]
            else:
                return False
        return curr.word
                
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        # Traverse through the Trie to search for word
        curr = self.root
        for char in prefix:
            if curr.children[ord(char)-ord('a')] != None:
                curr = curr.children[ord(char)-ord('a')]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
