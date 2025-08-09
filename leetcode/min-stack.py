class MinStack:

    def __init__(self):
        # Main stack to store all pushed values
        self.stack = []
        # Auxiliary stack to store the minimum value at each level
        self.minStack = []
        

    def push(self, val: int) -> None:
        # Push the actual value onto the main stack
        self.stack.append(val)
        # Determine the new minimum:
        # If minStack is not empty, compare current value with previous minimum
        # Otherwise, the current value is the minimum
        val = min(val, self.minStack[-1] if self.minStack else val)
        # Push the minimum so far onto minStack
        self.minStack.append(val)
        

    def pop(self) -> None:
        # Remove the top value from both stacks to keep them in sync
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        # The top of minStack always holds the current minimum value
        return self.minStack[-1]