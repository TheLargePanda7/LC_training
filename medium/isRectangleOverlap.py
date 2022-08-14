class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1_r1 = rec1[0]
        x1_r2 = rec2[0]
        
        y1_r1 = rec1[1]
        y1_r2 = rec2[1]
        
        x2_r1 = rec1[2]
        x2_r2 = rec2[2]
        
        y2_r1 = rec1[3]
        y2_r2 = rec2[3]
        
        
        # Edge case
        # If coordinate of bottom left is the same as coordinate of top right, then we know there is no area. Since no area is produced, it is not possible to have overlap
        if (x1_r1 == x2_r1 or y1_r1 == y2_r1) or (x1_r2 == x2_r2 or y1_r2 == y2_r2):
            return False
        
        # Condition for rectangle to be NOT overlap
        return not (x2_r1 <= x1_r2 or y2_r1 <= y1_r2 or x1_r1 >= x2_r2 or y1_r1 >= y2_r2)
