class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, res = {}, 0  # `count` keeps frequency of chars in the current window, `res` stores max length found
        l = 0               # Left pointer of the sliding window

        # Right pointer expands the window
        for r in range(len(s)):
            # Add or update the count of the current character
            count[s[r]] = 1 + count.get(s[r], 0)

            # Check if the number of characters we need to replace (total window - most frequent char count) > k
            while (r - l + 1) - max(count.values()) > k:
                # If yes, shrink the window from the left
                count[s[l]] -= 1
                l += 1

            # Update the result with the maximum valid window size so far
            res = max(res, r - l + 1)

        return res  # Return the length of the longest valid substring