from heapq import heapify, heappush, heappop
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        """
        Things to do (based on the hint):
        1. Allocate rooms meetings that occur earlier in the way (Simple sort should do the job)
        2. Only two options: pick existing meeting room or allocate a new one
        3. If there is available meeting, pick the earliest one (Can do it with hashmap, but we may need to sort it every single time. Other way is to use min heap because it automatically adjust nodes for us. The top of the heap is always the minimum value)
        
        Algorithms:
        1. Sort the intervals array by their start-time
        2. Create a heap using python library
        3. Iterate through sorted interval array and compare the start time of i element to the end-time of the top node in the min heap. If intervals[i].start() < heap_top_node.end(), we will allocate a new room by pushing a new element to the heap. By now, the heap should automatically adjust its structure and change the top node accordingly. If
intervals[i].start() > heap_top_node.end(), it indicates there is a room available, just replace the top min heap node with the new interval
        """
        if not intervals:
            return 0
        
        # Step 1
        intervals = sorted(intervals, key = lambda x:x[0])
        cnt = 0
        
        # Step 2
        heap = []
        heapify(heap)
        first_end_time = intervals[0][1]
        heappush(heap,first_end_time)
        cnt += 1
        # Step 3
        for i in range(1,len(intervals)):
            curr_start_time = intervals[i][0]
            curr_end_time = intervals[i][1]
            min_heap_node = heap[0] # Always minimum
            
            if curr_start_time < heap[0]:
                # Conflict detected, need to allocate a new room
                cnt +=1 
                heappush(heap,curr_end_time)
            else:
                # Room is available
                pop_element = heappop(heap)
                heappush(heap,curr_end_time)
                
        
        return cnt
            
        
        
        
        
