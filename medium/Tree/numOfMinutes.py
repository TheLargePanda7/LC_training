import math
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Time start: 7:00
        """
        
        n -> number of employees (including the headID)
        manager array -> manager of i-th employee
        informTime array -> time needed for employee i-th to inform all
        """
        queue = deque()
        queue.append((headID,informTime[headID]))
        dict = defaultdict(list)
        currCnt = 0
        
        # Build tree
        for i in range(len(manager)):
            parent = manager[i]
            child = i
            dict[parent].append(child)
            
            
        while queue:
            id, time = queue.popleft()
            currCnt = max(currCnt,time)
            for key in dict[id]:
                queue.append((key,time + informTime[key]))
                
                
                
                
        return currCnt        
                        
                        
                    
        
        
