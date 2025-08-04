class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i] will store the number of 1 bits in the binary representation of i
        dp = [0] * (n + 1)

        # 'offset' tracks the most recent power of 2 (1, 2, 4, 8, ...)
        # because the pattern of bit counts repeats after each power of 2
        offset = 1

        # Iterate over every number from 1 to n
        for i in range(1, n + 1):
            # If i hits the next power of 2, update the offset
            if offset * 2 == i:
                offset = i

            # Formula:
            # Number of 1s in i = 1 (for the MSB set at 'offset') 
            # + number of 1s in (i - offset), which reuses a previously computed value
            dp[i] = 1 + dp[i - offset]

        # Return list of bit counts for all numbers [0..n]
        return dp