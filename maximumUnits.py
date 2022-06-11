class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        """
        truckSize -> number of boxes can be put onto the truck
        Goal: we want to maximize the number of units
        
        Example:
        [[5,10],[2,5],[4,7],[3,9]] truckSize = 10
        
        5 * 10 = 50 : Remaining space = 5
        3 * 9 = 27 : Remaning space = 2
        2 * 7 =  14 : Remaning space = 0
        
        Total units = 91
        
        Notice that we always prioritize the box type with the maximum units first
        
        This is a greedy choice problem
        
        We can sort the array based on the maximum units, we will have:
        
        [[5,10],[3,9],[4,7],,[2,5]]
        
        Iterate through them, if we have enough space, take them all. Otherwise, just take how many boxes we can
        
        
        Example 2:
        [[5,10],[2,5],[4,7],[3,9]] 10
        
        [[5,10],[3,9],[4,7],[2,5]]
        
        5 * 10 = 50 (R: 5)
        3 * 9 = 27 (R:2)
        2 * 7 = 14 (R:0)
        
        Expected 91
        
        """
        boxTypes_sorted = sorted(boxTypes,key = lambda x: x[1], reverse = True)
        print(boxTypes_sorted)
        
        max_units = 0
        
        for i in range(len(boxTypes_sorted)):
            number_boxes = boxTypes_sorted[i][0]
            units = boxTypes_sorted[i][1]
            if truckSize == 0:
                break
            if truckSize - number_boxes > 0:
                # Take all boxes
                max_units += units * number_boxes
                truckSize -= number_boxes
                #print("units", max_units)
                #print("truck size", truckSize)
            else:
                # Cannot take all boxes. Can only take whatever we have left
                max_units += truckSize * units
                truckSize = 0
                
            print(max_units)
        return max_units
                
                
