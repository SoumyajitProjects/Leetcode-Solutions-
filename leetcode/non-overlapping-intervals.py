class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by start time
        intervals.sort()

        res = 0                     # Count of intervals removed
        prevEnd = intervals[0][1]   # Track the end of the last valid interval

        # Step 2: Iterate through all intervals (starting from the 2nd one)
        for start, end in intervals[1:]:
            # Case 1: No overlap → update prevEnd to the current interval's end
            if start >= prevEnd:
                prevEnd = end
            else:
                # Case 2: Overlap → remove one interval
                res += 1
                # Keep the interval with the smaller end to maximize space 
                # for upcoming intervals
                prevEnd = min(end, prevEnd)
        
        # Step 3: Return total number of removed intervals
        return res