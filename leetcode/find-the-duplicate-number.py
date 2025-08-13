class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Tortoise and Hare (cycle detection) over the "next" relation: next(i) = nums[i]
        # Phase 1: find an intersection point inside the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]            # move 1 step
            fast = nums[nums[fast]]      # move 2 steps
            if slow == fast:             # pointers meet inside the cycle
                break
        
        # Phase 2: find the cycle entrance (the duplicate value)
        slow2 = 0
        while True:
            slow = nums[slow]            # move 1 step from meeting point
            slow2 = nums[slow2]          # move 1 step from start (index 0)
            if slow == slow2:            # meeting point is the cycle entrance
                return slow              # this value is the duplicate