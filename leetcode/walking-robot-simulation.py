class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:

        # Starting position of the robot
        x, y = 0, 0
        
        # 4 possible directions the robot can face:
        # North (0), East (1), South (2), West (3)
        direction = [
            [0, 1],   # North: move up
            [1, 0],   # East: move right
            [0, -1],  # South: move down
            [-1, 0]   # West: move left
        ]
        
        d = 0  # robot starts facing North
        res = 0  # track the maximum distance squared
        
        # Convert obstacle list to a set for O(1) lookup
        obstacles = {tuple(o) for o in obstacles}

        for c in commands:

            # Turn right
            if c == -1:
                d = (d + 1) % 4
            
            # Turn left
            elif c == -2:
                d = (d - 1) % 4
            
            # Move forward c steps
            else:
                dx, dy = direction[d]  # current direction vector
                
                for _ in range(c):
                    # Check if next step hits an obstacle
                    if (x + dx, y + dy) in obstacles:
                        break
                    
                    # Move one step forward
                    x += dx
                    y += dy

            # Update the farthest Euclidean distance squared from origin
            res = max(res, x * x + y * y)
        
        return res