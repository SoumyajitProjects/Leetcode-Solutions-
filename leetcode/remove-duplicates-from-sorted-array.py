class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: if the list is empty, return 0
        if not nums:
            return 0

        # l is the slow-runner pointer, starts at index 1 (first unique position)
        l = 1

        # r is the fast-runner pointer, starts from index 1
        for r in range(1, len(nums)):
            # If current number is different from the previous one (i.e., a new unique number)
            if nums[r] != nums[r - 1]:
                # Copy it to the l-th position
                nums[l] = nums[r]
                l += 1  # Move the slow pointer

        # l is the count of unique elements (new length of the array)
        return l