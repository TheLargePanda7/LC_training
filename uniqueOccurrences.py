class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        """
        1   :   1
        2   :   2
        3   :   3
        
        """
        dict = {}
        
        for i in range(len(arr)):
            if arr[i] not in dict:
                dict[arr[i]] = 1
            else:
                dict[arr[i]] += 1
        print(dict)
        
        original_arr = []
        for key in dict:
            original_arr.append(dict[key])
            
        
        unique_set = set(original_arr)
        print(unique_set)
        if len(unique_set) == len(original_arr):
            return True
        else:
            return False
        
