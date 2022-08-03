class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Goal: find the min of all subarrays of arr and sum them up
        
        # Base case
        arr = [0] + arr
        n = len(arr)
        
        # dp[i] -> keep track of the minimum of subarray ending at index i
        dp = [0 for i in range(n)]
        
        # Monotonic stack (maintain ascending order)
        mon_stack = [0]
        for i in range(n):
            while arr[i] < arr[mon_stack[-1]] and mon_stack:
                mon_stack.pop()
            prev_less_element_index = mon_stack[-1]
            
            # DP Formation #1 (i - prev is to get the distance from the current index to the index of prev less element) and multiplied by arr[i] to either represent current element itself or duplicated version of current element if it is minimum we have found so far (such as case [4,2,1] [2,1], and [1] where all three subarrays have min of 1) 
            # DP Fomration #2 (dp[prev] -> the result of previous subarray minimum)
            dp[i] = dp[prev_less_element_index] + ((i - prev_less_element_index) * arr[i])
            mon_stack.append(i)
            
        return sum(dp) % (pow(10,9) + 7)
            
            
        
        
