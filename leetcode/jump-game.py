class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Start with the goal being the last index
        goal = len(nums) - 1

        # Traverse the array backwards
        for i in range(len(nums) - 1, -1, -1):
            # If from index i, you can reach (or pass) the current goal,
            # update the goal to this index i
            if i + nums[i] >= goal:
                goal = i

        # If after traversing, the goal has moved all the way back to 0,
        # it means the first index can eventually reach the last index
        return True if goal == 0 else False