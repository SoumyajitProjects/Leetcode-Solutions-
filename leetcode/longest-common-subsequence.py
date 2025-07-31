class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D DP table initialized with zeros.
        # dp[i][j] will represent the LCS length between text1[i:] and text2[j:].
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Traverse text1 and text2 in reverse (bottom-up DP)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                
                # Case 1: If characters match, take 1 + diagonal result
                # (i.e., move to next indices in both strings)
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                
                # Case 2: Otherwise, skip one character (either from text1 or text2)
                # and take the max LCS length
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # The answer is stored at dp[0][0], meaning LCS of the full strings
        return dp[0][0]