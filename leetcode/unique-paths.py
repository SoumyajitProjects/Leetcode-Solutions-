class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the bottom row with all 1s
        # (Base case: from the last row, there's only 1 way to reach the destination for each cell — move right)
        row = [1] * n

        # Iterate from the second-to-last row up to the first row
        for i in range(m - 1):
            # Start a new row filled with 1s (base case for the rightmost column: only 1 way down)
            newRow = [1] * n
            # Traverse from right to left (excluding last column, already set to 1)
            for j in range(n - 2, -1, -1):
                # Number of paths from cell (i, j) = paths from right + paths from below
                newRow[j] = newRow[j + 1] + row[j]
            # Update current row for the next iteration
            row = newRow

        # The top-left cell (0,0) contains the total number of unique paths
        return row[0]