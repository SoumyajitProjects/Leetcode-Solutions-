class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()     # Set to keep track of unique characters in the current window
        l = 0               # Left pointer of the sliding window
        res = 0             # Variable to store the maximum length of substring found

        # Iterate through each character using the right pointer
        for r in range(len(s)):
            # If the character at the right pointer is already in the set, it's a duplicate
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove the leftmost character from the set
                l += 1                # Move the left pointer forward to shrink the window
            
            charSet.add(s[r])         # Add the current character to the set (it's now unique in the window)
            res = max(res, r - l + 1) # Update the result with the max window size found so far
        
        return res  # Return the length of the longest substring without repeating characters