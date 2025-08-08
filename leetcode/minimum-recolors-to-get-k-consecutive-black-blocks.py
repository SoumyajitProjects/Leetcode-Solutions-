class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Left pointer for sliding window
        l = 0
        # Number of white blocks ('W') in the current window
        recolor = 0
        # Result initialized to the worst case: recolor all k blocks
        res = k

        # Iterate with right pointer over each block
        for r in range(len(blocks)):
            # If the rightmost block is white, it would need recoloring
            if blocks[r] == 'W':
                recolor += 1

            # If window size has reached exactly k
            if r - l + 1 == k:
                # Update the minimum recolors needed
                res = min(res, recolor)

                # Before moving the left pointer, remove its contribution
                if blocks[l] == 'W':
                    recolor -= 1
                # Slide the window forward
                l += 1

        # Return the minimum number of recolors found
        return res