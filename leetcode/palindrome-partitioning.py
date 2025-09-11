class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []          # final result: list of all valid palindrome partitions
        partitions = []   # temporary list to hold the current partitioning

        def backtrack(i):
            # If we've reached the end of the string,
            # the current partitioning is valid → add a copy to results
            if i >= len(s):
                res.append(partitions[:])
                return 
            
            # Try all possible substrings starting at index i
            for j in range(i, len(s)):
                # If substring s[i..j] is a palindrome
                if self.isPali(s, i, j):
                    # Choose: add this palindrome to current partition
                    partitions.append(s[i:j+1])
                    # Recurse on the remaining substring starting at j+1
                    backtrack(j + 1)
                    # Backtrack: remove last added substring to try others
                    partitions.pop()

        # Start exploring from index 0
        backtrack(0)
        return res
    
    # Helper function: checks if substring s[l..r] is a palindrome
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:   # mismatch → not palindrome
                return False
            l, r = l + 1, r - 1
        return True