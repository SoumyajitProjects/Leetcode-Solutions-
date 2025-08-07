class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize two pointers for both strings
        i, j = 0, 0
        res = []  # This list will hold the merged characters

        # Loop through both strings as long as there are characters in both
        while i < len(word1) and j < len(word2):
            res.append(word1[i])  # Add one character from word1
            res.append(word2[j])  # Add one character from word2
            i += 1  # Move to next character in word1
            j += 1  # Move to next character in word2

        # Append the remaining characters from either word1 or word2
        # Only one of these will have any characters left
        res.append(word1[i:])  # Add remaining from word1 (if any)
        res.append(word2[j:])  # Add remaining from word2 (if any)

        # Join the list of characters into a single string and return
        return "".join(res)