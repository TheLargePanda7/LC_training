import random
class RandomizedSet(object):

    def __init__(self):
        self.rand_set = {}
        # We need to declare another data structure to help us compute random function in O(1)
        # We cannot do it in O(1) with hashmap because random function takes in a list and if we convert hashmap to list, we have O(n)
        self.arr = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        if val not in self.rand_set:
            self.rand_set[val] = 1 # Insert element into set
            self.arr.append(val)
            return True
        
        return False
        
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # Removes an item val from the set if present. Returns true if the item was present, false otherwise
        if val in self.rand_set:
            del self.rand_set[val]
            self.arr.remove(val)
            return True
        
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        # Same probability of being returned randomly
        rand_numb = random.choice(self.arr)
        return rand_numb
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
