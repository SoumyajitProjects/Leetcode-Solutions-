# Trie Node definition
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes for each character
        self.word = False   # Flag to mark the end of a valid word

    # Method to insert a word into the Trie
    def add(self, word):
        cur = self
        for c in word:
            # If character doesn't exist, create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]  # Move to the next node
        cur.word = True  # Mark the end of the word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        # Add all words into the Trie
        for w in words:
            root.add(w)

        # Dimensions of the board
        ROWS, COLS = len(board), len(board[0])
        res = set()     # Set to store found words (avoid duplicates)
        visited = set() # Track visited cells during DFS

        # DFS to explore the board
        def dfs(r, c, node, word):
            # Boundary and validity checks
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
                board[r][c] not in node.children or 
                (r, c) in visited):
                return 

            visited.add((r, c))  # Mark cell as visited
            node = node.children[board[r][c]]  # Move to the next Trie node
            word += board[r][c]  # Append current letter to the word

            # If the current path forms a complete word, add it to result
            if node.word:
                res.add(word)

            # Explore all 4 directions
            dfs(r + 1, c, node, word)  # Down
            dfs(r - 1, c, node, word)  # Up
            dfs(r, c + 1, node, word)  # Right
            dfs(r, c - 1, node, word)  # Left

            visited.remove((r, c))  # Backtrack (unmark visited)

        # Start DFS from each cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)  # Convert set to list and return