class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the maximum subarray sum with the first element
        maxSub = nums[0]
        # Keep track of the current subarray sum
        curSum = 0

        # Iterate through each number in the array
        for n in nums:
            # If the running sum becomes negative, reset it
            # (since starting fresh from current number is better than carrying a negative sum)
            if curSum < 0:
                curSum = 0

            # Add current number to the running sum
            curSum += n
            # Update maxSub if the current sum is greater
            maxSub = max(maxSub, curSum)

        # Return the maximum subarray sum found
        return maxSub