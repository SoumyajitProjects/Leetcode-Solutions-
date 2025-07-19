import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for the smaller half of numbers (invert sign to simulate max-heap with min-heap)
        self.small = []  
        # Min-heap for the larger half of numbers
        self.large = []

    def addNum(self, num: int) -> None:
        # If `large` is non-empty and num is greater than the smallest in `large`,
        # insert it into `large` (min-heap)
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # Otherwise, insert it into `small` (max-heap, simulated using negative values)
            heapq.heappush(self.small, -1 * num)

        # Balance the heaps: if `small` has more than 1 extra element, move one to `large`
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)  # Convert back to positive
            heapq.heappush(self.large, val)

        # Balance the heaps: if `large` has more than 1 extra element, move one to `small`
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)  # Store as negative to simulate max-heap

    def findMedian(self) -> float:
        # If `small` has more elements, median is top of max-heap (convert back to positive)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # If `large` has more elements, median is top of min-heap
        elif len(self.large) > len(self.small):
            return self.large[0]
        # If both heaps are equal, median is the average of two middle values
        return (-1 * self.small[0] + self.large[0]) / 2.0