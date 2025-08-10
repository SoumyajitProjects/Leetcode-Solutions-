class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize search space: left pointer l, right pointer r
        l, r = 0, len(nums) - 1

        # Continue searching while the window is valid
        while l <= r:
            # Middle index
            m = (l + r) // 2

            # If the middle element is greater than target,
            # then target must be in the left half
            if nums[m] > target:
                r = m - 1

            # If the middle element is less than target,
            # then target must be in the right half
            elif nums[m] < target:
                l = m + 1

            # If nums[m] == target, we found it → return index
            else:
                return m

        # Target not found in the array
        return -1