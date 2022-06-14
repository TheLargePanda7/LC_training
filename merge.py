class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # This approach has time complexity of O(n*log(n)) using sorted function
        # Space is O(n) because we declare a new array to store a new thing
        
        # To make things easier, we will sort the array based on the start time for each interval
        intervals = sorted(intervals, key = lambda x: x[0])
        
        if len(intervals) == 1:
            return intervals
        
        res = []
        res.append(intervals[0])
        
        for i in range(1,len(intervals)):
            curr_start = intervals[i][0]
            previous_end = res[-1][1]
            # Check if there is overlap
            if curr_start <= previous_end:
                curr_end = intervals[i][1]
                
                # Check which end-time to use for the new interval (merged version)
                if curr_end < previous_end:
                    new_end = previous_end
                else:
                    new_end = intervals[i][1]
                
                new_start = res[-1][0]
                res.pop(-1) # No longer need the previous one, we can replace it with the merged version
                res.append([new_start,new_end])
            else:
                # Nothing happens (no overlap)
                res.append(intervals[i])
                
        return res
