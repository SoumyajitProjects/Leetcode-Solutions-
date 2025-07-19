class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # Get board dimensions
        path = set()  # Track visited cells in the current search path to avoid revisiting

        def dfs(r, c, i):
            # If we've matched all characters in the word, return True
            if i == len(word):
                return True
            
            # Boundary and constraint checks:
            # - Out of bounds
            # - Current cell doesn't match the word character
            # - Already visited this cell in current path
            if (min(r, c) < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False
            
            # Mark the current cell as visited
            path.add((r, c))

            # Explore all 4 directions (down, up, right, left)
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # Backtrack: remove the current cell from path so it can be reused elsewhere
            path.remove((r, c))
            return res

        # Start DFS from each cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # Try to match the word starting at (r, c)
                    return True
        return False  # No path found