class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Reverses the list of characters using the two-pointer approach.
        """

        # Initialize two pointers: left at the start, right at the end of the list
        l, r = 0, len(s) - 1

        # Loop until the two pointers meet in the middle
        while l < r:
            # Swap the characters at the left and right pointers
            s[l], s[r] = s[r], s[l]

            # Move the left pointer to the right
            l += 1
            # Move the right pointer to the left
            r -= 1

        # No return needed since the operation is in-place