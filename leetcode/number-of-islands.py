class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If the grid is empty, return 0 islands
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])  # Get dimensions of the grid
        visit = set()  # Set to keep track of visited cells
        islands = 0    # Counter for number of islands

        # Breadth-First Search helper function
        def bfs(r, c):
            q = collections.deque()  # Initialize a queue for BFS
            visit.add((r, c))        # Mark the starting cell as visited
            q.append((r, c))         # Enqueue the starting cell

            # Process the queue
            while q:
                row, col = q.popleft()  # Dequeue the front cell
                # Define the four possible directions to move (down, up, right, left)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc  # Compute new cell coordinates
                    # If the new cell is in bounds, is land ("1"), and not visited
                    if (r in range(rows) and c in range(cols) and 
                        grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))   # Add the new cell to the queue
                        visit.add((r, c))  # Mark it as visited

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land and hasn't been visited yet
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)      # Launch BFS to explore the entire island
                    islands += 1   # Increment island count after a full BFS

        return islands  # Return total number of islands found