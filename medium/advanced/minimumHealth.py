class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        
        """
        Greedy Choice -> use the armor whenever the damage at current level i is greater or equal to the armor damage block
        For example (Case 1 where armor does not block dmg at level i completely):
        dmg = [2,7,4,3] 
        
        i = 0:
        dmg_intake = 2
        
        i = 1:
        use armor
        dmg_intake = 2 + (7-4) = 5
        
        i = 2:
        dmg_intake = 5 + 4 = 9
        
        i = 3:
        dmg_intake = 9 + 3 = 12
        
        But you need to survive, hence, minimum health is 12 + 1 = 13
        
        What happens if there are no damage that is greater than armor itself?
        
        For example (Case 2 where armor blocks dmg at level i completely):
        dmg = [2,5,3,4], armor = 7
        2 + [useArmor() -> 0 dmg] + 3 + 4 = 2 + 0 + 3 + 4 = 9
        Min health = 10
        
        """
        
        max_dmg = 0
        level = 0
        
        for i in range(len(damage)):
            dmg = damage[i]
            if dmg > max_dmg:
                max_dmg = dmg
                level = i
                
        if armor > damage[level]:
            # Case 2 (where armor completely blocks dmg)
            damage.pop(level)
        else:
            # Case 1 (where armor does not block dmg completely)
            damage[level] -= armor
            
        
        min_health = 0
        for dmg_intake in damage:
            min_health += dmg_intake
            
        return min_health + 1
    
        
