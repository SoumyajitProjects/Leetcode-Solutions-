class Solution:
    def rob(self, nums: List[int]) -> int:

        # In a circular arrangement, the first and last houses are adjacent.
        # So we can't rob both. We take the max of two scenarios:
        # 1. Rob from house 1 to house n-1 (exclude first house)
        # 2. Rob from house 0 to house n-2 (exclude last house)
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        # Helper function for standard House Robber (non-circular)
        rob1, rob2 = 0, 0  # rob1 = max until i-2, rob2 = max until i-1

        for n in nums:
            # Choose between robbing this house (n + rob1) or skipping it (rob2)
            temp = max(rob1 + n, rob2)
            rob1 = rob2      # Update for next iteration
            rob2 = temp
        return rob2