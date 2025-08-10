class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Result array, initialized to 0 (default: no warmer day found)
        res = [0] * len(temperatures)
        # Stack will store pairs [temperature, index] for days awaiting a warmer day
        stack = []

        # Iterate through all temperatures with their index
        for i, t in enumerate(temperatures):
            # While the stack is not empty and the current temperature is warmer
            # than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()  # Remove that cooler day
                # Set the number of days waited until a warmer temperature
                res[stackIndex] = i - stackIndex
            # Push the current day's temperature and index onto the stack
            stack.append([t, i])
        
        # Return the result array
        return res