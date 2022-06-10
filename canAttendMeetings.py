class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        
        """
            General approach
            We will first sort the intervals based on the start time, so we have:
            [[7,10],[2,4]] -> [[2,4],[7,10]]
            
            Then we start iterating at i = 1 and compare its start time with the previous end time.
            If arr[i].start > arr[i-1].end -> this is okay
            Otherwise return false
            After iteration, remember to assign the new previous end time
            
        """
        
        if (len(intervals)) == 1 or (len(intervals)) == 0:
            return True
        sorted_intervals = sorted(intervals,key = lambda x: x[0])
        print(sorted_intervals)
        previous_end = sorted_intervals[0][1]
        
        for i in range(1,len(sorted_intervals)):
            current_start = sorted_intervals[i][0]
            print(previous_end,current_start)
            if current_start < previous_end:
                return False
            previous_end = sorted_intervals[i][1]
            
        return True
            
        
        
        
