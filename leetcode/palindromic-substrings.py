class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0  # Counter to store the total number of palindromic substrings

        # Iterate through each character in the string to consider it as a center
        for i in range(len(s)):
            # ----- Count odd-length palindromes (center at i) -----
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1       # Found a palindrome, increment result
                l -= 1         # Expand left
                r += 1         # Expand right

            # ----- Count even-length palindromes (center between i and i+1) -----
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1       # Found a palindrome, increment result
                l -= 1         # Expand left
                r += 1         # Expand right

        return res  # Return the total count of palindromic substrings