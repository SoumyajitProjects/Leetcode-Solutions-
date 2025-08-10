class TimeMap:

    def __init__(self):
        # Map each key -> list of [value, timestamp] pairs in ascending timestamp order
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Initialize the list for a new key
        if key not in self.store:
            self.store[key] = []
        # Append at the end (LeetCode guarantees non-decreasing timestamps for a key)
        self.store[key].append([value, timestamp])
      

    def get(self, key: str, timestamp: int) -> str:
        # Default if no suitable timestamp is found
        res = ""
        # Fetch the history for this key (empty list if key unknown)
        values = self.store.get(key, [])

        # Binary search for the RIGHTMOST timestamp <= given timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                # Candidate answer: keep value, but try to find a later (closer) timestamp
                res = values[m][0]
                l = m + 1
            else:
                # Too new: move left
                r = m - 1
        return res