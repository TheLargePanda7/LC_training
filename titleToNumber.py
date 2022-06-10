import math
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        """
        Pattern:
        A -> Z      :   1 -> 26
        AA -> AZ    :   27 -> 52
        BA -> BZ    :   53 -> 78
        CA -> CZ    :   ...
        DA -> DZ    :   ...
        
        (26 * level) + letter position
        If we have two digits, we know that 27th position is the starting position
        
        Z = 26
        AA = 27
        
        ZZ = 702
        AAA = 703
        
        General Approach:
        
        1 char title -> we have 26 columns
        2 char title -> we have 626 columns (because AA to ZZ gives us that much)
        3 char title -> 17576
        ...
        
        As we observe more, we have the general formula to determine # of columns 26^(char_title)
        char_title can be determined using the digit position. 
        For example, if we have AZZC, A is in 3rd position, Z is in 2nd position, and so on
        Break it down we have:
        # columns = 1 ('A') * 26^3 (3 is the char title) + 26 ('Z') * 26^2 + 26 ('Z') * 26^1 + 3 ('C') + 26^0 (0th represents 0 char title)
    
        
        """
        dictionary = {
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4,
            'E' : 5,
            'F' : 6,
            'G' : 7,
            'H' : 8,
            'I' : 9,
            'J' :10,
            'K' :11,
            'L' :12,
            'M' :13,
            'N' :14,
            'O' :15,
            'P' :16,
            'Q' :17,
            'R' :18,
            'S' :19,
            'T' :20,
            'U' :21,
            'V' :22,
            'W' :23,
            'X' :24,
            'Y' :25,
            'Z' :26
            
        }
        column_res = 0
        n = len(columnTitle)
        j = 0
        
        # Backward iteration
        for i in reversed(range(n)):
            # j is th ith position of the coressponding character (goes from right to left)
            column_res += dictionary[columnTitle[i]] * math.pow(26,j)
            
            j+= 1            
        
        
        return int(column_res)
            
            
            
        
        
        
