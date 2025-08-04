class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Start result with the length of nums
        # (This accounts for the last index 'n' in the range [0..n])
        res = len(nums)

        # Iterate through the array
        for i in range(len(nums)):
            # Add the index and subtract the actual number at that index
            # Effectively computing: sum(0..n) - sum(nums)
            res += (i - nums[i])

        # The leftover value in res is the missing number
        return res