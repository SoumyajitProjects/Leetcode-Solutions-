class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize result to 0
        res = 0

        # Loop through all 32 bits (since input is a 32-bit unsigned integer)
        for i in range(32):
            # Extract the i-th bit from n:
            # (n >> i) shifts n to the right by i places, so the i-th bit moves to the least significant position
            # & 1 masks everything except that least significant bit
            bit = (n >> i) & 1

            # Place the extracted bit into its reversed position:
            # (31 - i) ensures the bit from position i is placed in the mirrored position
            res = res | (bit << (31 - i))

        # Return the reversed 32-bit integer
        return res