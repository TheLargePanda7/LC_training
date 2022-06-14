class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        """
        To do this in-place, we will apply two pointers technique
        First, we will have a left pointer poiting at s[0] and right pointer pointing at s[-1]
        
        We swap the value at these pointers together and increment left pointer and decrement right pointer until they met in the middle (odd case) or pass each other (even case)
        
        """
        left = 0
        right = len(s) - 1
        
        while left != right and left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -=1
        
        
            
            
        
