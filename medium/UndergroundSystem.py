from decimal import Decimal
class UndergroundSystem(object):

    def __init__(self):
        # Key = id and value = (stationName,time)
        """
        check_in = {
            45: ("Leyton",3)
            32: ("Paradise",8)
            27: ("Leyton",10)
        }
        storage = {
            "Leyton->Waterloo": [12,14,..],
            
        }
        
        Customer: "Leyton" -> "Waterloo" and arrival time = 12
        
        undergroundSystem.checkOut(45, "Waterloo", 15);
        check_in[45] = ("Leyton",3)
        from = stationName
        to = check_in[45][0]
        # Need to store the from and to stationName and the arrival time somewhere
        
        
        arrival_time = t - check_in[45][1] # 15 - 3 = 12
        
        # Once a customer checks out, we remove id from check_in dictionary so that they can re-check-in next time
        # We need to update storage
        storage["->".join(from,to)].append(arrival_time)
        
        """
        
        
        self.check_in = {}
        self.average_storage = defaultdict(list)
        
        
        
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id not in self.check_in:
            self.check_in[id] = (stationName,t)
        else:
            print("ERROR, this customer is already checked in ")
            
        
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        # A customer cannot check out without checking in first
        if id in self.check_in:
            start_time = self.check_in[id][1]
            arrival_time = t - start_time
            path = "->".join((self.check_in[id][0],stationName)) # Paradise->Cambridge
            self.average_storage[path].append(arrival_time)
            # Because a customer already checks out, we need to remove the customer from check_in dictionary so that they can check in again later
            del self.check_in[id]
        else:
            print("ERROR, this customer has not checked in yet! ")
            
        

    def getAverageTime(self, startStation, endStation):
        
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        
        
        path = "->".join((startStation,endStation))
        average = 0
        if path in self.average_storage:
            # In python2, float / int will give us a decimal number
            # But, float // int will floor the result down
            average = float(sum(self.average_storage[path])) / len(self.average_storage[path])
            
            print("Actual array:", self.average_storage[path])
            print("Sum of array",float(sum(self.average_storage[path])))
            print("Denominator",len(self.average_storage[path]))
            print("Average",average)
            print("-----")
            
        return average
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
