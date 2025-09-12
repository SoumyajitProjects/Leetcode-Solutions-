class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])

        # DFS helper function to mark safe 'O's connected to the border
        def capture(r, c):
            # Stop if out of bounds or not an 'O'
            if (r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O"):
                return 
            
            # Temporarily mark the cell as 'T' (safe, not to be flipped)
            board[r][c] = "T"

            # Explore all 4 directions (down, up, right, left)
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Capture unsurrounded regions
        # Run DFS from any 'O' on the border (they can't be flipped)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)

        # Step 2: Flip all remaining 'O' → 'X' (they are surrounded)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Step 3: Convert 'T' back to 'O' (safe regions connected to border)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"