class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers for binary search
        l, r = 0, len(nums) - 1

        # Standard binary search loop
        while l <= r:
            # Calculate middle index
            m = (l + r) // 2

            # If the middle element is the target, return its index
            if target == nums[m]:
                return m

            # Check if the left half is sorted
            if nums[l] <= nums[m]:
                # If target is outside the left sorted half, discard it
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    # Target is in the left sorted half
                    r = m - 1

            # Otherwise, the right half must be sorted
            else:
                # If target is outside the right sorted half, discard it
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    # Target is in the right sorted half
                    l = m + 1

        # If we exit the loop, the target is not in the array
        return -1