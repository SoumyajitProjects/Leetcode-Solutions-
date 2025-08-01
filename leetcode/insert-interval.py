class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # Final list of merged intervals

        for i in range(len(intervals)):
            # Case 1: New interval comes completely before current interval
            # (no overlap, just add newInterval and the rest of intervals can follow untouched)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # Case 2: New interval comes completely after current interval
            # (no overlap, keep adding intervals as they are)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 3: Overlap case
            # Merge the overlapping intervals by expanding newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # smallest start
                    max(newInterval[1], intervals[i][1])   # largest end
                ]

        # If newInterval hasn't been inserted yet, add it at the end
        res.append(newInterval)
        return res