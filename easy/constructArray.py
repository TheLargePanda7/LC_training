class Solution(object):
    
    def constructArray(self,key,n,res):
        for i in range(n):
            res.append(key)
        return
    
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        [4,5,9]
        [4,4,8,9,9]
        
        dict1 = {
            4 : 1
            5: 1
            9: 1
        }
        
        dict2 = {
            4: 2
            8: 1
            9: 2
        
        }
        First approach using double hashmaps
        res = []
        dict1 = {}
        dict2 = {}
        
        for num in nums1:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
                
        for num in nums2:
            if num not in dict2:
                dict2[num] = 1
            else:
                dict2[num] += 1
        print(dict1)
        print(dict2)
                
        for key in dict1:
            if key in dict2:
                numElement = 0
                if dict1[key] > dict2[key]:
                    numElement = dict2[key]
                else:
                    numElement = dict1[key]
                self.constructArray(key,numElement,res)
                
        return res
        """
        
        """
        Second approach using pointers with sort
        Have two pointers pointing to the begining of each array
        Move pointer if one element of array 1 is smaller than current element of array 2 (this is because the nature of sorting)
        If two elements are the same, move both
        """
        nums1.sort()
        nums2.sort()
        res = []
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            print(i,j)
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return res
        
        
    
