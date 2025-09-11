class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []  # this will hold all possible letter combinations

        # Mapping from digit to possible characters (like on a phone keypad)
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",   # note: normally this is "pqrs", check typo if needed
            "8": "tuv",
            "9": "wxyz",
        }

        # Backtracking function
        # i = current index in the digits string
        # curString = current combination built so far
        def backtrack(i, curString):
            # Base case: if we've used all digits,
            # save the built string and return
            if i >= len(digits):
                res.append(curString[:])  # append a copy
                return 
            
            # Recursive case: try all possible chars for the current digit
            for ch in digitToChar[digits[i]]:
                # move to the next digit with current char added
                backtrack(i + 1, curString + ch)
            
        # Only run backtracking if digits is non-empty
        if digits:
            backtrack(0, "")
        
        return res