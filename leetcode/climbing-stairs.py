class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: there's 1 way to climb 0 or 1 steps
        one, two = 1, 1  # one = ways to reach current step, two = ways to reach previous step

        # Iterate from step 2 to n (n - 1 iterations)
        for i in range(n - 1):
            temp = one              # Temporarily store current 'one'
            one = two + one         # Total ways to current step = one step + two steps before
            two = temp              # Update 'two' to be the old 'one'

        return one  # Return the number of ways to reach step n