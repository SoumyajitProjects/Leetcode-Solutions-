class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Number of rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])

        # Step 1: Binary search to find the correct row
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2  # mid row

            # If target is greater than the last element of the mid row,
            # it must be in a lower row
            if target > matrix[row][-1]:
                top = row + 1

            # If target is less than the first element of the mid row,
            # it must be in a higher row
            elif target < matrix[row][0]:
                bot = row - 1

            # Target could be in this row
            else:
                break

        # If we exited without finding a valid row
        if not (top <= bot):
            return False

        # Step 2: Binary search within the found row
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2  # mid column index

            if target > matrix[row][m]:
                l = m + 1  # search right
            elif target < matrix[row][m]:
                r = m - 1  # search left
            else:
                return True  # found target

        return False  # not found