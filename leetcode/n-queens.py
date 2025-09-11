class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to track columns and diagonals already under attack by a queen
        column = set()         # columns with queens
        positiveDiag = set()   # (r + c) → "\" diagonals
        negativeDiag = set()   # (r - c) → "/" diagonals

        res = []  # stores all valid board configurations
        # build an n×n chessboard initially filled with "."
        board = [["."] * n for i in range(n)]

        # Recursive backtracking function, placing queens row by row
        def backtrack(r):
            # Base case: all n queens placed successfully
            if r == n:
                # Convert the board (2D list) into list of strings and save
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            # Try placing a queen in each column of the current row
            for c in range(n):
                # Skip if this column or diagonals are already attacked
                if c in column or (r + c) in positiveDiag or (r - c) in negativeDiag:
                    continue
                
                # Place queen at (r, c)
                column.add(c)
                positiveDiag.add(r + c)
                negativeDiag.add(r - c)
                board[r][c] = "Q"

                # Move on to the next row
                backtrack(r + 1)

                # Backtrack: remove queen and free constraints
                column.remove(c)
                positiveDiag.remove(r + c)
                negativeDiag.remove(r - c)
                board[r][c] = "."

        # Start placing queens from the first row
        backtrack(0)
        return res