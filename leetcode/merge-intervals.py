class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by their start time
        intervals.sort(key=lambda i: i[0])

        # Step 2: Initialize output with the first interval
        output = [intervals[0]]

        # Step 3: Process each interval one by one (starting from the 2nd)
        for start, end in intervals[1:]:
            lastend = output[-1][1]  # Get the end of the last interval in output

            # Case 1: Overlapping interval → merge
            if start <= lastend:
                # Extend the last interval’s end if needed
                output[-1][1] = max(lastend, end)
            
            # Case 2: No overlap → add new interval
            else:
                output.append([start, end])
        
        # Step 4: Return merged intervals
        return output