class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Get the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # Set to keep track of visited cells so we don't revisit them
        visit = set()

        # Depth-First Search function to compute the area of an island
        def dfs(r, c):
            # Base case: if out of bounds, water cell, or already visited
            if (r < 0 or r == ROWS or c < 0 or c == COLS or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            # Mark the cell as visited
            visit.add((r, c))
            
            # Count this cell (1) and recursively search in all 4 directions
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + 
                        dfs(r, c + 1) + dfs(r, c - 1))
        
        maxArea = 0  # Initialize the maximum area found

        # Iterate over every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # Start a DFS if the cell is land and not visited
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea  # Return the largest island area found