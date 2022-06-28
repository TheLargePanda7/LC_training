class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r,c,prefix):
            cols = len(board[0])
            rows = len(board)
            # Base Case
            if len(prefix) == 0:
                return True
            
            # Boundary Checking
            if r < 0 or c < 0 or c >= cols or r >= rows or board[r][c] != prefix[0]:
                return False
            board[r][c] = "visited"
            
            North = dfs(r-1,c,prefix[1:]) # North
            South = dfs(r+1,c,prefix[1:]) # South
            East = dfs(r,c-1,prefix[1:]) # West
            West = dfs(r,c+1,prefix[1:]) # East
            # Backtracking
            board[r][c] = prefix[0]
            
            return North or South or East or West
            
        cols = len(board[0])
        rows = len(board)
        
        visited = []
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "visited":
                    if dfs(r,c,word):
                        return True
        return False
