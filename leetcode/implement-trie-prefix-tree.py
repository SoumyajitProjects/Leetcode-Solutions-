# Node class representing each character node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}        # Dictionary to map character -> TrieNode
        self.endOfWord = False    # Flag to mark the end of a complete word


# Trie (Prefix Tree) class
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the root node of the Trie

    # Inserts a word into the Trie
    def insert(self, word: str) -> None:
        cur = self.root  # Start from the root

        for c in word:
            # If character not already a child of current node, add it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]  # Move to the child node
        cur.endOfWord = True  # Mark the end of the word

    # Returns True if the word exists in the Trie
    def search(self, word: str) -> bool:
        cur = self.root  # Start from the root

        for c in word:
            # If character doesn't exist in children, word is not present
            if c not in cur.children:
                return False
            cur = cur.children[c]  # Move to the child node
        return cur.endOfWord  # Only return True if current node marks end of word

    # Returns True if there is any word in the Trie that starts with the given prefix
    def startsWith(self, prefix: str) -> bool:
        cur = self.root  # Start from the root

        for c in prefix:
            # If character doesn't exist in children, no such prefix
            if c not in cur.children:
                return False
            cur = cur.children[c]  # Move to the child node
        return True  # All characters in prefix were found