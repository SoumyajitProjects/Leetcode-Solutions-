class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        # Directions for spiral traversal:
        # Right, Down, Left, Up
        directions = [
            [0, 1],   # move right
            [1, 0],   # move down
            [0, -1],  # move left
            [-1, 0]   # move up
        ]

        res = []  # result list storing visited coordinates in spiral order
        r, c = rStart, cStart  # starting cell

        steps = 1      # number of steps to take in the current "leg" of the spiral
        i = 0          # index for current direction (0 = right, 1 = down, ...)

        # Continue until we've collected every valid cell in the matrix
        while len(res) < rows * cols:

            # For each step count, we move in the current direction twice
            # Example pattern: 1 step right, 1 step down, 2 left, 2 up, 3 right, 3 down, ...
            for _ in range(2):

                # Extract current direction vector
                dr, dc = directions[i]

                # Move `steps` times in the current direction
                for _ in range(steps):

                    # Add current position *only if inside matrix bounds*
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])

                    # Move 1 step in the direction
                    r, c = r + dr, c + dc

                # Rotate direction clockwise (right -> down -> left -> up)
                i = (i + 1) % 4

            # After two legs of movement, increase step count
            steps += 1

        return res