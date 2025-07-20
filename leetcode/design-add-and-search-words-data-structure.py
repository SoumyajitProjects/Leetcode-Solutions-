# Trie node definition
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to map each character to its corresponding TrieNode
        self.word = False   # Flag to indicate the end of a valid word

# WordDictionary class using Trie to store and search words (supports '.' wildcard)
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  # Initialize the root node of the Trie

    # Adds a word to the Trie
    def addWord(self, word: str) -> None:
        cur = self.root  # Start at the root

        # Traverse the word character by character
        for c in word:
            # If the character is not present in current node's children, create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]  # Move to the next node
        cur.word = True  # Mark the end of the word

    # Searches for a word in the Trie, where '.' can match any letter
    def search(self, word: str) -> bool:

        # Helper function to perform DFS with support for '.' wildcard
        def dfs(j, root):
            cur = root  # Start from the given node

            # Traverse each character from index j to end
            for i in range(j, len(word)):
                c = word[i]

                # If the current character is '.', try all possible child nodes
                if c == ".":
                    for child in cur.children.values():
                        # Recursively search from the next index for each child
                        if dfs(i + 1, child):
                            return True
                    return False  # No match found for wildcard
                else:
                    # If the character does not exist in current children, return False
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]  # Move to the matched child node

            # After the loop, check if the current node marks the end of a word
            return cur.word

        # Start DFS from root at index 0
        return dfs(0, self.root)