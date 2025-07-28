class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a DP array of size (amount + 1) filled with a large value.
        # We use amount + 1 as an effective "infinity" placeholder since we can't use more than amount coins.
        dp = [amount + 1] * (amount + 1)

        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        # Build up the DP table from amount 1 to amount
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # Update dp[a] to the minimum number of coins needed
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] was not updated, return -1 (no combination can form the amount)
        return dp[amount] if dp[amount] != amount + 1 else -1