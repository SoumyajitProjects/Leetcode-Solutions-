class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # Create a dictionary that maps characters -> thier occurances
        count = {}

        # Loop through the string 
        for i in range(len(s)):
            # Build out the dictionary
            count[s[i]] = 1 + count.get(s[i], 0)
        
        # Next loop through the dictionary
        for c in count:
            # Check to see if any of the characters have an occurance of exactly 1 -> This is the first unique character 
            if count[c] == 1:
                # if so we return the index of the letter from the orignal string 
                return s.index(c)
        # There is no unique character so we return -1 
        return -1

        """

        TC:
        First Loop builds count dict: O(N)
        Second Loop iterates over dict (up to 26 keys): O(1)
        s.index(c) -> O(N) can be called up worst case 26 times: O(N x 26) = O(N)
        Therefore TC -> O(N)

        SC -> O(1), since we use only lowercase letters 
        """