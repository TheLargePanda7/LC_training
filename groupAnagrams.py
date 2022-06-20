class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        
        """
            Observation:
            Two strings are the anagram of each other iff their characters frequency is the same
            Or their sorted version are the same
            
            Algorithms:
            We can declare a dictionary because we want to optimize our look-up time
            Iterate through the given array and sort each of them. Look up in dictionary to see if its sorted string already exists in the dictionary, if it is, append to the same group. Otherwise, create a new group
            Finally iterate through dictionary to append all groups to the result array
            
            
        """
        if len(strs) == 1:
            return [strs]
        
        dict = {}
        dict[''.join(sorted(strs[0]))] = [strs[0]]
        
        for i in range(1,len(strs)):
            
            if ''.join(sorted(strs[i])) in dict:
                dict[''.join(sorted(strs[i]))].append(strs[i])
            else:
                dict[''.join(sorted(strs[i]))] = [strs[i]]
        res = []
        for key in dict:
            res.append(dict[key])
        return res
        
        
            
            
        
        
        
