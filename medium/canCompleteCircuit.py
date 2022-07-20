class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        totalCost = 0 # The total cost of the entire journey (same regardless station we pick)
        currTank = 0 # If it is possible to move to next station given the current gas we have in the tank
        pick_index = 0
        
        for i in range(len(gas)):
            # Remaining in gas will be equal to the gas we just fill at station i and the cost to go to next station i + 1
            totalCost += gas[i] - cost[i]
            currTank += gas[i] - cost[i]
            if currTank < 0:
                # We have no gas anymore, we must pick the next station
                pick_index = i + 1
                # Reset this so that we can keep counting the gas we have as we continue traveling
                currTank = 0
                
        if totalCost < 0:
            # It is not possible to have a path that we can complete the journey since the amount of cost is greater than resources
            return -1
        return pick_index
    
                
                
        
        
        
        
        
        
    
        
