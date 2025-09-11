class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []        # stores all unique subsets
        nums.sort()     # sort so duplicates are adjacent (important for skipping)

        def backtrack(i, subset):
            # Base case: if we've considered all elements
            if i >= len(nums):
                res.append(subset[:])  # add a *copy* of current subset
                return 
            
            # Choice 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)   # move to next index
            subset.pop()               # backtrack (remove nums[i])

            # Choice 2: skip nums[i]
            # Skip over any duplicates so we don't generate duplicate subsets
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        # Start recursion with index 0 and empty subset
        backtrack(0, [])
        return res