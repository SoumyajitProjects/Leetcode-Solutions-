class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1: max money that can be robbed from houses up to i - 2
        # rob2: max money that can be robbed from houses up to i - 1
        rob1, rob2 = 0, 0

        for n in nums:
            # If we rob this house (n + rob1) vs skip it (rob2)
            temp = max(n + rob1, rob2)
            # Update rob1 to previous rob2 (i-1 becomes i-2 for next iter)
            rob1 = rob2
            # rob2 becomes the best of robbing or skipping current house
            rob2 = temp

        # rob2 holds the max amount of money we can rob
        return rob2