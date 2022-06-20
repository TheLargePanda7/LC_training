class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int -> space available for big car
        :type medium: int -> space available for medium car
        :type small: int -> space available for small car
        """
        
        """
        1 -> big
        2 -> medium
        3 -> small
        """
        
        self.big_size = big
        self.med_size = medium
        self.small_size = small
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        # Big car
        if carType == 1:
            if self.big_size != 0:
                self.big_size -= 1
            else:
                # Full
                return False
        # Medium car
        if carType == 2:
            if self.med_size != 0:
                self.med_size -= 1
            else:
                # Full
                return False
        
        # Small car
        if carType == 3:
            if self.small_size != 0:
                self.small_size -= 1
            else:
                # Full
                return False
            
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
