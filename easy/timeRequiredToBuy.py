class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        i = 0 is priority to buy tickets than i > 0
        tickets[0] -> 0th person wants to buy tickets[0] tickets
        For example:
        tickets[0] = 2 -> 0th person wants to buy 2 tickets
        
        Dry-run:
        queue = [0,1,2] -> [2,3,2] tickets and k = 2
        We want to find the number of seconds that 2th person can buy all tickets he/she wants
        
        FIFO
        Original [0,1,2] -> [2,3,2]
        
        time = 1
        queue = [1,2,0] -> [1,3,2]
        
        time = 2
        queue = [2,0,1] -> [1,2,2]
        
        time = 3
        queue = [0,1,2] -> [1,2,1]
        
        time = 4
        queue = [1,2] -> [0,2,1]
        
        time = 5
        queue = [2,1] -> [0,1,1]
        
        time = 6
        queue = [1,2] -> [0,1,0]
        
        Done
        
        """
        time = 0
        queue = deque()
        dict = {}
        
        
        for i in range(len(tickets)):
            if i not in dict:
                """
                tickets = [2,3,2]
                dict = {
                    0: 0,
                    1: 1,
                    2: 0
                }
                queue = [0,1,2]
                queue = [1,2,0]
                queue = [2,0,1]
                queue = [0,1,2]
                queue = [1,2]
                queue = [2,1]
                queue = [1]
                
                
                """
                dict[i] = tickets[i]
            queue.append(i)
        
        while queue:
            time += 1
            ith_person = queue.popleft()
            if ith_person in dict:
                
                dict[ith_person] -= 1 # buy tickets for person i
                if dict[k] == 0: # if the target already bought all tickets, just return the time
                    return time
                
                if dict[ith_person] > 0:
                    queue.append(ith_person) # still have tickets to buy                
                
                
            
        
        
        
    
        
