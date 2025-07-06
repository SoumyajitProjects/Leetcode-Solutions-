class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the input list to a set for O(1) lookups
        num_set = set(nums)

        # Initialize a variable to track the longest consecutive sequence
        longest = 0

        # Iterate over each unique number in the set
        for num in num_set:
            # Only attempt to build a sequence from numbers that are the start of a sequence
            if num - 1 not in num_set:
                # This number is the start of a sequence
                current = num
                streak = 1

                # Check for consecutive numbers in the set
                while current + 1 in num_set:
                    current += 1      # Move to the next consecutive number
                    streak += 1       # Increment the streak count

                # Update the longest streak if this one is longer
                longest = max(longest, streak)

        # Return the length of the longest consecutive sequence found
        return longest