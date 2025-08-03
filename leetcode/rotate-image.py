class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Left and right pointers to track the current "layer" (outer to inner)
        l, r = 0, len(matrix) - 1

        # Process layer by layer until the middle is reached
        while l < r:
            # For each element in the current layer (excluding last one, handled by rotation)
            for i in range(r - l):
                top, bottom = l, r  # Top and bottom row indices

                # Save the top-left value (will be overwritten first)
                topLeft = matrix[top][l + i]

                # Move bottom-left → top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom-right → bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top-right → bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move saved top-left → top-right
                matrix[top + i][r] = topLeft

            # Move inward to the next layer
            l += 1
            r -= 1