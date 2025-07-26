class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""       # Stores the longest palindromic substring found
        resLen = 0     # Stores the length of the longest palindrome

        for i in range(len(s)):
            # ----- Check for odd-length palindrome -----
            # Center is at i (e.g., "racecar", center at 'e')
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update result if this palindrome is longer than previous
                if (r - l + 1 > resLen):
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1  # Expand to the left
                r += 1  # Expand to the right

            # ----- Check for even-length palindrome -----
            # Center is between i and i+1 (e.g., "abba", center between 'b's)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update result if this palindrome is longer than previous
                if (r - l + 1 > resLen):
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1  # Expand left
                r += 1  # Expand right

        return res  # Return the longest palindromic substring found