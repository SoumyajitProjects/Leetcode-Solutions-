class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize an array to store the LIS value for each index
        # LIS[i] represents the length of the Longest Increasing Subsequence starting at index i
        LIS = [1] * len(nums)

        # Traverse the array from right to left
        for i in range(len(nums) - 1, -1, -1):
            # Compare nums[i] with every number that comes after it
            for j in range(i + 1, len(nums)):
                # If nums[i] < nums[j], it can be part of an increasing subsequence
                if nums[i] < nums[j]:
                    # Update LIS[i] with the maximum length found
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # The result is the maximum value in the LIS array
        return max(LIS)