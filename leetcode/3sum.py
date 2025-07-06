class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []               # This will store all the valid triplets that sum to zero
        nums.sort()            # Sort the input list to make two-pointer logic work

        for i, a in enumerate(nums):
            # Skip duplicates for the first number to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1  # Initialize two pointers: left and right
            while l < r:
                threeSum = a + nums[l] + nums[r]  # Calculate the sum of the triplet

                if threeSum > 0:
                    r -= 1  # Sum too big, move right pointer left to decrease sum
                elif threeSum < 0:
                    l += 1  # Sum too small, move left pointer right to increase sum
                else:
                    # Found a triplet that sums to 0, add it to result
                    res.append([a, nums[l], nums[r]])
                    l += 1  # Move left pointer to continue looking for other combinations

                    # Skip duplicate values at left pointer to avoid duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res