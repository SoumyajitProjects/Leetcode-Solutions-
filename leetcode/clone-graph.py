"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary to map original nodes to their cloned counterparts
        oldToNew = {}

        # Depth-First Search recursive function
        def dfs(node):
            # If node has already been copied, return the copy
            if node in oldToNew:
                return oldToNew[node]
            
            # Create a new copy of the current node
            copy = Node(node.val)
            # Store it in the map to avoid duplication and infinite loops
            oldToNew[node] = copy

            # Recursively copy all the neighbors
            for nei in node.neighbors:
                # Append the cloned neighbor to the current node's neighbors list
                copy.neighbors.append(dfs(nei))
            
            return copy  # Return the cloned node

        # If input node is None, return None, else start DFS from the node
        return dfs(node) if node else None