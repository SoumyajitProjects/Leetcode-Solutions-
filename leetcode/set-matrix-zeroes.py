class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])  
        rowZero = False   # Flag to track if the first row should be zeroed

        # Step 1: Mark rows and columns that need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Mark column in first row
                    matrix[0][c] = 0
                    # Mark row in first column (if not the first row itself)
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        # If the zero is in the first row, mark the flag
                        rowZero = True
        
        # Step 2: Use the markers to set cells to zero (skip first row/col for now)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Step 3: Handle the first column separately (if top-left is 0, zero the column)
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # Step 4: Handle the first row separately (if rowZero flag is set)
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0