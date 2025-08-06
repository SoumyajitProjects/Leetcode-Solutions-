class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Initialize two pointers: one at the start, one at the end of the array
        left, right = 0, len(numbers) - 1

        # Iterate until the two pointers meet
        while left < right:
            current_sum = numbers[left] + numbers[right]

            # If the current sum is less than the target, move the left pointer to the right
            if current_sum < target:
                left += 1

            # If the current sum is greater than the target, move the right pointer to the left
            elif current_sum > target:
                right -= 1

            # If the current sum equals the target, return the 1-indexed positions
            else:
                return [left + 1, right + 1]

        # If no solution is found (shouldn't happen given problem constraints), return empty list
        return []