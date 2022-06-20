from heapq import heapify, heappush, heappop

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        """
        
        Example:
        points = [[3,3],[5,-1],[-2,4]], k = 2
        
        d (3,3) = 4.24
        d (5,-1) = 5.099
        d (-2,4) = 4.47
        
        Since k = 2, we pick d (3,3) and  d (-2,4) 
        
        Initial thought:
        We will iterate through the array and calculate the distance of each pair x and y. We will append the result distance to the min heap (this is crucial because we want to return the min distance)
        As we are done, iterate through k in order to pop elements from the heap and append to the array
        
        """
        
        heap = []
        heapify(heap)
        dict = {}
        for i in range(len(points)):
            # Calculate the distance for each coordinate
            dist = math.sqrt(math.pow(0-points[i][0],2) + math.pow(0-points[i][1],2))
            # We use dictionary for look-up later when we try to remove element from the heap
            if dist not in dict:
                dict[dist] = [[points[i][0],points[i][1]]] 
            else:
                # Remember that coordinates can have the same distance
                dict[dist].append([points[i][0],points[i][1]])
            
            heappush(heap,dist)
        res = []
        print(dict)
        #print(len(heap))
        while k > 0:
            min_dist = heappop(heap)
            if len(dict[min_dist]) != 0:
                remove_element = dict[min_dist].pop() # get one of the coordinate based on min distance
            res.append(remove_element)
            
            k -=1
        return res
            
             
