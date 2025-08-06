class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use hash sets to keep track of seen numbers in:
        # - each row
        # - each column
        # - each 3x3 subgrid ("square")
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (row_block, col_block)

        # Loop through all 9 rows and 9 columns
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue
                
                # Check if the current value already exists in
                # the same row, same column, or same 3x3 square
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False  # Invalid if duplicate found
                
                # Otherwise, add the number to the respective row, col, and square
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        # If no violations found, the Sudoku board is valid
        return True