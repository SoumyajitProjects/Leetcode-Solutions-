class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize result with the first element (a valid default)
        res = nums[0]

        # Set left and right pointers for binary search
        l, r = 0, len(nums) - 1

        # Continue searching while the window is valid
        while l <= r:
            # If the current window is already sorted (not rotated)
            if nums[l] < nums[r]:
                # The smallest element is at the left
                res = min(res, nums[l])
                break  # We can stop early

            # Compute the middle index
            m = (l + r) // 2

            # Update the result with the minimum seen so far
            res = min(res, nums[m])

            # Determine which half is sorted and discard it
            if nums[m] >= nums[l]:
                # Left half is sorted, so minimum must be in right half
                l = m + 1
            else:
                # Right half is sorted, search the left half
                r = m - 1

        # Return the minimum value found
        return res