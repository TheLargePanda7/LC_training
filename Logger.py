class Logger(object):
    """
        If message i is being printed out at T, then the same message cannot be printed until T + 10
        
    """
    def __init__(self):
        # Declare a dictionary where key-value is a timestamp and key is a message itself
        self.time_tracker = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        """
        time_tracker {
            "foo": 11
            "bar": 12
        }
        
        """
        if message not in self.time_tracker:
            self.time_tracker[message] = timestamp + 10
        else:
            # Message is already being added to tracker, we need to check its existing timestamp to make sure it is okay to print
            current_time = self.time_tracker[message]
            if timestamp < current_time:
                return False
            else:
                self.time_tracker[message] = timestamp + 10
        return True
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
