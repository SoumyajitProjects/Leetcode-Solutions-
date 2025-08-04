class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0   # Counter to keep track of how many 1 bits we find

        # Keep looping until n becomes 0
        while n:
            # Trick: n & (n-1) removes the rightmost set bit (1) in n
            n = n & (n - 1)

            # Each time we remove a 1-bit, increment the count
            res += 1

        # Return the total number of 1 bits
        return res