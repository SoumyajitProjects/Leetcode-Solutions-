class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0  # Initialize variable to store the maximum area found so far
        l, r = 0, len(heights) - 1  # Set two pointers: left at start, right at end

        while l < r:
            # Calculate the area between the lines at l and r
            # Width is (r - l), height is the smaller of the two lines
            area = (r - l) * min(heights[l], heights[r])
            
            # Update the result if this area is greater than the current max
            res = max(res, area)

            # Move the pointer pointing to the shorter line inward
            # This might lead to a taller line and potentially a larger area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res  # Return the maximum area found