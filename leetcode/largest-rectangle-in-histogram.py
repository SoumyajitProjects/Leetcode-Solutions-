class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # stack holds pairs: (start_index, height)

        # Scan bars left → right
        for i, h in enumerate(heights):
            start = i
            # If current bar is lower than the stack's top height,
            # we must close rectangles that used that taller height.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # width is from 'index' up to (but not including) i
                maxArea = max(maxArea, height * (i - index))
                # the next rectangle of height h can start as far left as 'index'
                start = index
            # Push current bar with the farthest left start it can extend to
            stack.append((start, h))

        # Close any remaining rectangles that rise to the end
        n = len(heights)
        for i, h in stack:
            # width is from i to n-1 inclusive → length (n - i)
            maxArea = max(maxArea, h * (n - i))

        return maxArea