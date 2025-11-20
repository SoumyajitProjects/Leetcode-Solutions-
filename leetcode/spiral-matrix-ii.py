class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # Create an n x n matrix initialized with zeros
        matrix = [[0] * n for _ in range(n)]

        # Boundary pointers for the spiral traversal
        left, right = 0, n - 1
        top, bottom = 0, n - 1

        # Value to fill the matrix with
        val = 1

        # Continue filling while the boundaries are valid
        while left <= right and top <= bottom:
            
            # 1. Fill the top row from left to right
            for c in range(left, right + 1):
                matrix[top][c] = val
                val += 1
            top += 1  # Top boundary moves down

            # 2. Fill the right column from top to bottom
            for r in range(top, bottom + 1):
                matrix[r][right] = val
                val += 1
            right -= 1  # Right boundary moves left

            # 3. Fill the bottom row from right to left
            # Only run this loop if the row still exists
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    matrix[bottom][c] = val
                    val += 1
                bottom -= 1  # Bottom boundary moves up

            # 4. Fill the left column from bottom to top
            # Only run this loop if the column still exists
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    matrix[r][left] = val
                    val += 1
                left += 1  # Left boundary moves right

        return matrix