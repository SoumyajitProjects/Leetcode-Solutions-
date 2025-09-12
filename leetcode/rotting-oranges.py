class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()  # Queue for BFS (stores positions of rotten oranges)
        time, fresh = 0, 0  # Track elapsed time (minutes) and count of fresh oranges

        # Step 1: Count fresh oranges and collect initial rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:  # Fresh orange found
                    fresh += 1
                if grid[r][c] == 2:  # Rotten orange found
                    q.append([r, c])  # Add its position to BFS queue

        # Directions for neighbors (right, left, down, up)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Step 2: BFS - spread rotting process minute by minute
        while q and fresh > 0:
            # Process all rotten oranges at the current time step
            for i in range(len(q)):
                r, c = q.popleft()
                # Check all 4 adjacent cells
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Skip if out of bounds or not a fresh orange
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or 
                        grid[row][col] != 1):
                        continue

                    # Rot the fresh orange
                    grid[row][col] = 2
                    q.append([row, col])  # Add to queue to rot its neighbors later
                    fresh -= 1  # One less fresh orange to worry about

            # After finishing this layer (1 minute passes)
            time += 1

        # Step 3: If no fresh oranges remain, return time, else return -1
        return time if fresh == 0 else -1