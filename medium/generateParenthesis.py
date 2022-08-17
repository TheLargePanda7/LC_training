class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(res,arr,n,openCnt,closeCnt):
            #nonlocal openCnt, closeCnt
            # Base case
            if openCnt == n and closeCnt == n:
                res.append("".join(arr.copy()))
                return
            
            if openCnt < n:
                arr.append("(")
                backtrack(res,arr,n,openCnt + 1,closeCnt)
                arr.pop()
                
            if closeCnt < openCnt:
                arr.append(")")
                backtrack(res,arr,n,openCnt,closeCnt + 1)
                arr.pop() # Important
                
        res = []
        arr = []
        backtrack(res,arr,n,0,0)
        
        return res
