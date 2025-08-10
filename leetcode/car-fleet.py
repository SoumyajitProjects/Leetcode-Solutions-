class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up each car's (position, speed)
        pair = [[p, s] for p, s in zip(position, speed)]
        # Stack will hold the "arrival times" to the target of fleets (from right to left)
        stack = []

        # Sort cars by position ASC, then iterate from the car closest to target to farthest (right→left)
        for p, s in sorted(pair)[::-1]:
            # Time for this car to reach the target if it goes alone
            time = (target - p) / s
            stack.append(time)

            # If the current car's time is <= the time of the car ahead,
            # it will catch up and merge into that fleet → pop (no new fleet)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # Number of fleets is the number of distinct times left in the stack
        return len(stack)