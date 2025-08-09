class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []  # current sequence of parentheses being built
        res = []    # stores all valid combinations

        # backtrack(openN, closedN) generates valid parentheses recursively
        # openN   = number of '(' used so far
        # closedN = number of ')' used so far
        def backtrack(openN, closedN):
            # If we've used n '(' and n ')', we have a complete valid string
            if openN == closedN == n:
                res.append("".join(stack))  # join list into string and save it
                return 
            
            # Add '(' if we still have '(' left to place
            if openN < n:
                stack.append("(")               # choose '('
                backtrack(openN + 1, closedN)   # recurse with one more '('
                stack.pop()                     # undo choice (backtrack)
            
            # Add ')' only if there are unmatched '(' to close
            if closedN < openN:
                stack.append(")")               # choose ')'
                backtrack(openN, closedN + 1)   # recurse with one more ')'
                stack.pop()                     # undo choice (backtrack)
        
        # Start recursion with 0 '(' and 0 ')'
        backtrack(0, 0)
        return res