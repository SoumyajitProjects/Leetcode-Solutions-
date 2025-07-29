class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a DP array where dp[i] indicates whether s[i:] can be segmented using wordDict
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: empty string can be segmented

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            # Try every word in the dictionary
            for w in wordDict:
                # Check if the substring starting at i matches the current word
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # If the rest of the string after this word can be segmented, mark dp[i] as True
                    dp[i] = dp[i + len(w)]

                # If we've found a valid break at index i, no need to check more words
                if dp[i]:
                    break

        # If dp[0] is True, the whole string can be segmented using words from wordDict
        return dp[0]