class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create Dictionary to store groups of anagrams
        anagram_dict = {}

        # Loop through each word in strs
        for word in strs:
            # Sort the word 
            key = ''.join(sorted(word))
            # Use the sorted word as the key to group anagrams in the dictionary 
            if key not in anagram_dict:
                anagram_dict[key] = []
            anagram_dict[key].append(word)
        # Return final list 
        return list(anagram_dict.values())