class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []

        # Mapping of closing brackets to their corresponding opening brackets
        CloseToOpen = {")": "(", "]": "[", "}": "{"}

        # Iterate through each character in the input string
        for c in s:
            # If the character is a closing bracket
            if c in CloseToOpen:
                # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == CloseToOpen[c]:
                    stack.pop()  # Valid pair found, pop the opening bracket
                else:
                    return False  # Invalid pair or unmatched closing bracket
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(c)

        # After processing all characters, the stack should be empty for a valid string
        if not stack:
            return True  # All brackets matched
        return False  # Unmatched opening brackets remain