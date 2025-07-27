class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization dictionary to store results of subproblems
        # Base case: an empty string has 1 valid decoding (doing nothing)
        dp = {len(s): 1}
        
        # Recursive DFS function with memoization
        def dfs(i):
            # If we've already computed this subproblem, return the cached result
            if i in dp:
                return dp[i]
            
            # If the current character is '0', it cannot be decoded
            if s[i] == "0":
                return 0 
            
            # Try taking one digit (always valid if not '0')
            res = dfs(i + 1)

            # Try taking two digits if it's a valid number between 10 and 26
            if (i + 1 < len(s) and 
                (s[i] == "1" or 
                 (s[i] == "2" and s[i + 1] in "0123456"))):
                res += dfs(i + 2)

            # Store the result in the memoization table
            dp[i] = res
            return res
        
        # Start decoding from index 0
        return dfs(0)