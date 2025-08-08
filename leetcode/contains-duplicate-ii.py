class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # A set to store the elements in the current sliding window
        window = set()

        # Left pointer of the sliding window
        l = 0
        
        # Iterate with the right pointer over the array
        for r in range(len(nums)):

            # If window size exceeds k, remove the leftmost element
            # This ensures window only holds the last k elements
            if r - l > k:
                window.remove(nums[l])
                l += 1  # Move left pointer forward

            # If the current number already exists in the window,
            # it means we've seen this number within the last k indices → return True
            if nums[r] in window:
                return True

            # Add the current number to the window
            window.add(nums[r])

        # If we finish the loop without finding a nearby duplicate
        return False