class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
            Time Complexity: O(n)
            Space Complexity: O(n) -> dictionary
        """
        dict = defaultdict(list)
        
        for word in strs:
            dict["".join(sorted(word))].append(word)
        
        return dict.values()
            
        
        
