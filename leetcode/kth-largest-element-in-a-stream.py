class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the KthLargest object with:
        - k: the "k" for the kth largest element
        - nums: initial list of numbers
        """
        self.minHeap = nums       # Use a min-heap to track k largest numbers
        self.k = k
        heapq.heapify(self.minHeap)  # Convert nums into a heap in-place (O(n) time)

        # Keep only the k largest elements in the heap
        # The smallest element in the heap is the kth largest overall
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove smallest elements until heap size = k

    def add(self, val: int) -> int:
        """
        Add a new value to the stream and return the kth largest element.
        """
        heapq.heappush(self.minHeap, val)  # Add the new value to the heap

        # If heap exceeds size k, remove the smallest element
        # This ensures the heap always contains the k largest elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The root of the min-heap is the kth largest element
        return self.minHeap[0]