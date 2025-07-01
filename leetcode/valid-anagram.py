class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimized Solution: Using Hashmap 

        # Check if the strings match in length (Base Case):
        if len(s) != len(t):
            # If Strings do not match in length then they are not anagrams 
            return False 
        
        # Create two dictionaries for each string to keep track of the characters and the frequency of the characters
        countS, countT = {}, {}

        # Loop through the string 
        for i in range(len(s)):
            # Take the current count of the charcater and add 1 to it 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Compare frequecy maps:
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True 
        # TC -> O(N)
        # SC -> O(N)

        """
        Brute Force Solution:

        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

        TC -> O(N log N)
        SC -> O(N)
        """