class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        detected = False
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                index = nums2.index(nums1[i])
                if index != len(nums2) - 1:
                    for j in range(index+1,len(nums2)):
                        if nums2[j] > nums2[index]:
                            res.append(nums2[j])
                            detected = True
                            break
                    if detected == False:
                        res.append(-1)
                    else:
                        detected = False
                else:
                    res.append(-1)
                    
        return res
                    
                    
                
                
        
        
