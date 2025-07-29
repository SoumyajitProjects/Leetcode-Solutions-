class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize result as the maximum number in the array to handle edge cases (like all negatives)
        res = max(nums)

        # curMax and curMin track the max and min product ending at the current position
        # This is necessary because a negative number can flip min into max and vice versa
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                # Reset both max and min when we hit zero because any product with 0 becomes 0
                curMax, curMin = 1, 1
                continue 

            # Save current max multiplied by n (before updating curMax)
            temp = n * curMax

            # Compute new curMax: maximum of (n * curMax), (n * curMin), or just n
            curMax = max(n * curMax, n * curMin, n)

            # Compute new curMin: minimum of (temp), (n * curMin), or just n
            curMin = min(temp, n * curMin, n)

            # Update global result if current max is higher
            res = max(res, curMax, curMin)

        return res