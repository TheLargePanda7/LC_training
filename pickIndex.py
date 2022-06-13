import random
class Solution(object):

    """
        First, we need to notice that the higher the value is, the more chance its index will get picked
        Assume we have this array = [1,2,3] and have a line representing buckets for each number:
        
        |---|---------|------------|
        0   1         3            6
        
        If a number is landed somewhere between 0 and 1, we pick index 0. 
        If a number is landed somewhere between 1 and 3, then we pick index 1 and so on
        
        Notice that 2 (index 1) gets picked as twice as much as 1 (index 0). Same thing can be said for 6 (index 2)
        
        How to represent the line above? It is simple because if we look at the mark we see that it is just accumulated sum of arr[i] + arr[i-1]
        
        How to get a random number? Since we know that max is 6, we want to pick any value from 0 to 6 (above the line) by multiplying 6 by a random value between 0.0 to 1.0, which gives us a target value chosen randomly between 0 and 6.
        
        The goal is to simulate the experiment shown above
        
    """
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.max_mark = 0
        self.lines = []
        acc = 0
        for i in range(len(w)):
            acc += w[i]
            self.lines.append(acc)
        self.max_mark = self.lines[-1]
        

    def pickIndex(self):
        """
        :rtype: int
        """
        random_seed = random.random() # Pick value from 0.0 to 1.0
        target = self.max_mark * random_seed # Chosen number in range from 0 to max mark
        
        """
        Linear Scan
        for i in range(len(self.lines)):
            # Chosen candidate
            if self.lines[i] > target:
                return i
        """
        
        # Binary Search (Optimized approach)
        L_ptr = 0
        R_ptr = len(self.lines)
        
        while L_ptr < R_ptr:
            mid = (R_ptr + L_ptr) // 2
            
            if target < self.lines[mid]:
                R_ptr = mid
            else:
                L_ptr = mid + 1
        
        return L_ptr
    
                
        
        
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
