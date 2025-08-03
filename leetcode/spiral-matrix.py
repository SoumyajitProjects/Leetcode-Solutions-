class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []  # Result list to store spiral order

        # Define boundaries of the current "layer"
        left, right = 0, len(matrix[0])   # Column boundaries
        top, bottom = 0, len(matrix)      # Row boundaries

        # Continue until the boundaries collapse
        while left < right and top < bottom:
            # Traverse from left → right across the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # Shrink the top boundary (row has been processed)

            # Traverse from top → bottom along the rightmost column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # Shrink the right boundary (column has been processed)

            # Check again (matrix might collapse after above steps)
            if not (left < right and top < bottom):
                break

            # Traverse from right → left across the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # Shrink the bottom boundary

            # Traverse from bottom → top along the leftmost column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # Shrink the left boundary

        return res