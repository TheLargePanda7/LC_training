class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        
        n: 1 -> 3
        
        nodes   tree
        1       1
        2       2
        3       5
        
        """
        # have extra element to account for Numbtree(0) (Base case)
        dp = [0 for i in range(n+1)]
         
        # 0 node or 1 node -> 1 unique BST (Base case init)
        dp[0] = 1
        dp[1] = 1
        
        
        # Outer-for-loop: size of our current subproblem
        for nodes in range(2,n+1):
            # Picking a root node to build our Tree
            for root in range(1,nodes+1):
                # DP formation
                
                # Use the previous computed solution to help solve current problem
                left = dp[root-1]
                right = dp[nodes-root]
                
                # Produce all possible combination (multiplication)
                dp[nodes] += left * right
                
                
        return dp[n]
