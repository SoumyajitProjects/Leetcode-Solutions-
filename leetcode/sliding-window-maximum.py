class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []                     # Stores the maximums for each sliding window
        l = r = 0                     # Left and right pointers for the sliding window
        q = collections.deque()       # Monotonic decreasing deque (stores indices)

        while r < len(nums):
            # Maintain decreasing order in deque:
            # Remove indices from the back while the current value is larger
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)               # Add current index to deque

            # Remove leftmost index if it’s outside the current window
            if l > q[0]:
                q.popleft()
            
            # Once we’ve filled the first window, record the maximum
            if (r + 1) >= k:
                res.append(nums[q[0]])  # Front of deque is the max in the current window
                l += 1                  # Move left pointer to slide the window
            
            r += 1                      # Always move right pointer
        return res