class TicTacToe(object):

    def __init__(self, n):
        
        """
        :type n: int -> Dimension
        """
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diag = 0
        self.anti_diag = 0
        self.n = n
        
    #Follow-up: Could you do better than O(n2) per move() operation?
    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        return 0 if no one has yet won the game
        return x if winner x is determined 
        """
        # Do not need to check if the move is valid because it is guaranteed to be one
        
        # Once a winning condition is reached, no more moves are allowed.
        
        # Requirement that move has to be done in O(1) in space complexity
        
        """
        Naive Approach:
            Create 2-D array and place a value to represent player n. Each time move() is called, naively call a helper method to check horizontally, vertically, diagonally, and anti-diagonally if a winner is found. 
            
        Optimization:
            We observe that a player is a winner if they marked all of the cells in a row or col n times. 
            The same thing can be said with diagonal and anti-diagonal
            So we create 2 arrays rows and cols to represent the number of times that player a or b has marked
            For example, if n = 3 we have row = [,,] and col = [,,]
            player 1 marked (0,0) now we have row = [1,,] and col = [1,,]
            player 2 marked (0,1) now we have row = [0,,] and col = [,-1,0]
            
            Note: we can keep track by incrementing the array element if player 1 moves and decrementing if player 2 moves
            At the end check both arrays, if one of the elements in row or col arrays is 3, then player 1 wins. Otherwise, if element is -3, player 2 wins
            Repeat the same process for diagonal (but just need to create a variable instead of array since one grid only has one way to win diagonally)
            NOTE: Essentially, each cell of row and col array represents difference in marks of player 1 and player 2
            Let's say in row 0, player 1 has marked 2 times and player 2 has marked only one time, then we expect row[0] = 1 (because 2 - 1 = 1)
        """
        move = 0
        if player == 1:
            move = 1
        else:
            move -= 1
        
        
        self.rows[row] += move
        self.cols[col] += move

        
        if row == col:
            # Diagonal
            self.diag += move
        if col == (self.n - row - 1):
            # Anti-diagonal
            self.anti_diag += move
            
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player


        return 0

            
            
                
                
        
        
        
        
        
                
        
        
            
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
