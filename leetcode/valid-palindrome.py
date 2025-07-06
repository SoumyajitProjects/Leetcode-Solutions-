class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: one at the start, one at the end of the string
        l, r = 0, len(s) - 1

        # Loop until the two pointers meet
        while l < r:
            # Move the left pointer forward if current character is not alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Move the right pointer backward if current character is not alphanumeric
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # Compare the characters at left and right (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False  # Not a palindrome if mismatch
            # Move both pointers toward the center
            l, r = l + 1, r - 1

        # If no mismatches were found, it's a palindrome
        return True

    # Helper function to check if a character is alphanumeric
    def alphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or  # Uppercase letters
            ord('a') <= ord(c) <= ord('z') or  # Lowercase letters
            ord('0') <= ord(c) <= ord('9')     # Digits
        )