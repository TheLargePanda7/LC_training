# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
            To minimize the call to API, we probably do not want to iterate and check elements one by one
            We can do a simple binary search by checking the middle element first
            If middle element is bad, we search the left
            Else, we search the right
            However, we need to declare a variable "curr" to keep track of the elements that we found bad recently so that in case we detect a good product, we can still return what we found previously (the first bad one)
            
        """
        
        left = 0
        right = n
        
        while left <= right:
            mid = (right + left) // 2
            
            if isBadVersion(mid):
                curr = mid # to keep track of current progress
                right = mid - 1
            else:
                left = mid + 1
        
        return curr
