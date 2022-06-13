from decimal import *
class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = []
        
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        avg = 0
        res = 0
        if len(self.queue) == self.size:
            # need to pop the front
            self.queue.pop(0)
            self.queue.append(val)
            for i in range(len(self.queue)):
                res += self.queue[i]
            avg = Decimal(res) / Decimal(self.size)
            
        elif len(self.queue) < self.size:
            # Either it is empty, 1, or 2
            # Do not need to pop. It is okay to add
            self.queue.append(val)
        
            for i in range(len(self.queue)):
                res += self.queue[i]
            avg = Decimal(res) / Decimal(len(self.queue))
            
            
            
        
        return avg
            
            
            
            
        
            
            
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
