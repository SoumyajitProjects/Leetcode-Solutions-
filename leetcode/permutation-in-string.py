class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s2 can't contain any permutation of s1
        if len(s1) > len(s2):
            return False

        # Frequency counts for s1 and the current window in s2
        s1Count, s2Count = [0] * 26, [0] * 26

        # Initialize counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Count how many character frequencies match between s1 and the first window of s2
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Sliding window: expand to the right and shrink from the left
        l = 0
        for r in range(len(s1), len(s2)):
            # If all 26 character counts match, s2 contains a permutation of s1
            if matches == 26:
                return True
            
            # Add the new character from the right side of the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1  # Frequency now matches exactly
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1  # We broke a previous match
            
            # Remove the character going out from the left side of the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1  # Frequency now matches exactly again
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1  # We broke a previous match
            l += 1  # Move left pointer forward
        
        # Final check for the last window
        return matches == 26