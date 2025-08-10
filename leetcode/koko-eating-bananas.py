class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search space: the slowest possible speed is 1 banana/hour
        # The fastest possible speed is max(piles) bananas/hour
        l, r = 1, max(piles)

        # Initialize result with the maximum speed
        res = r

        # Binary search to find the minimum valid eating speed
        while l <= r:
            # Middle speed to test
            k = (l + r) // 2

            # Calculate total hours needed at speed k
            hours = 0
            for p in piles:
                # Each pile takes ceil(p / k) hours
                hours += math.ceil(p / k)

            # If we can finish within h hours at speed k
            if hours <= h:
                # Update result with a smaller speed
                res = min(res, k)
                # Try slower speed (search left half)
                r = k - 1
            else:
                # Need more speed (search right half)
                l = k + 1

        return res  # Minimum speed found