class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1  # Initialize two pointers: l for buying day, r for selling day
        maxP = 0     # Variable to store the maximum profit found so far

        # Traverse the prices array starting from index 1
        while r < len(prices):
            # If the current selling price is greater than the buying price
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]  # Calculate the profit
                maxP = max(maxP, profit)        # Update max profit if current is higher
            else:
                # If selling price is lower, move the buying pointer to r (new minimum)
                l = r
            # Always move the selling pointer to the right
            r += 1

        return maxP  # Return the maximum profit found