class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Step 0: If endWord is not in wordList, no valid transformation exists
        if endWord not in wordList:
            return 0

        # Step 1: Build adjacency patterns for all words
        # Key: intermediate pattern with '*' replacing one character
        # Value: list of words matching that pattern
        nei = collections.defaultdict(list)
        wordList.append(beginWord)  # Include beginWord for neighbor mapping

        for word in wordList:
            for j in range(len(word)):
                # Create pattern by replacing one character with '*'
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        # Step 2: Initialize BFS
        visit = set([beginWord])   # Keep track of visited words to avoid cycles
        q = deque([beginWord])     # BFS queue starting from beginWord
        res = 1                    # Transformation length (starts at 1 for beginWord)

        # Step 3: BFS traversal
        while q:
            # Process all nodes at the current BFS level
            for i in range(len(q)):
                word = q.popleft()

                # Step 4: Check if we reached the target
                if word == endWord:
                    return res

                # Step 5: Explore neighbors using intermediate patterns
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            # Increment transformation length after finishing the current level
            res += 1

        # Step 6: If BFS ends without reaching endWord, return 0
        return 0