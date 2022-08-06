class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 1:
            return 0
        
        # Apply Greedy Choice + Sorting Technique
        
        # Sort the array based on the start time before the algorithm
        intervals = sorted(intervals, key = lambda x : x[0])
        # Represent the very first interval
        prev_s = intervals[0][0]
        prev_e = intervals[0][1]
        
        n = len(intervals)
        res = []
        cnt_removal = 0
        
        for i in range(1,n):
            curr_s = intervals[i][0]
            curr_e = intervals[i][1]
                
            # Overlap situation
            if curr_s < prev_e:
                # Compare their end time to see which one to take
                if curr_e < prev_e:
                    # Take current interval
                    prev_s = curr_s
                    prev_e = curr_e
                    
                    # Need to make decision of removing prev interval
                    cnt_removal += 1
                    
                elif curr_e >= prev_e:
                    # Take previous interval
                    # Need to make decision of removing curr interval
                    cnt_removal += 1
                # Another way to do this is to take the minimum of prev end time and curr end time
                # prev_e = min(prev_e,curr_e)
            elif curr_s >= prev_e:
                # Previous mistake: curr_s > prev_e (this does not take care of the case where prev and curr intervals are apart from each other - meaning there is a time gap between end of prev and start of curr interval)
                
                # No overlap situation
                # Update the prev_s and prev_e
                prev_s = curr_s
                prev_e = curr_e
                
        
        return cnt_removal
