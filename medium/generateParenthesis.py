class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Keep track of the count of open and close parenthesis
        open_parenthesis_cnt = 0
        close_parenthesis_cnt = 0
        res = []

        def backtrack(curr):
            nonlocal open_parenthesis_cnt, close_parenthesis_cnt
            if len(curr) == n * 2:
                res.append("".join(curr.copy()))
                return
            
            # At each position, we have two choices: "(" or ")"
            
            # First chpoce "("
            open_parenthesis_cnt += 1
            # If the cnt of close parenthesis is greater than open parenthesis, it is not in proper form
            if open_parenthesis_cnt >= close_parenthesis_cnt and open_parenthesis_cnt <= n:
                curr.append("(")
                backtrack(curr)
                # Backtrack to pick a second choice
                curr.pop()
            open_parenthesis_cnt -= 1
            
            # Second choice ")"
            close_parenthesis_cnt += 1
            # If the cnt of close parenthesis is greater than open parenthesis, it is not in proper form
            if open_parenthesis_cnt >= close_parenthesis_cnt and close_parenthesis_cnt <= n:
                curr.append(")")
                backtrack(curr)
                curr.pop()
            
            close_parenthesis_cnt -= 1
            
            
            
            
        curr = []
        backtrack(curr)
        
        return res
