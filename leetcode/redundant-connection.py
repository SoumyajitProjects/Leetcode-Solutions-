from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # Since graph has n nodes and n edges
        # Initialize adjacency list for graph representation
        adj_list = [[] for _ in range(n + 1)]

        def dfs(node: int, parent: int) -> bool:
            """
            Depth-First Search to detect a cycle.
            node   -> current node being visited
            parent -> the node we came from (to avoid trivial back edge)
            
            Returns True if a cycle is found.
            """
            if visit[node]:  
                # If we revisit a node, that means we found a cycle
                return True

            visit[node] = True  # Mark current node as visited

            # Explore all neighbors of this node
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    # Skip the edge we came from
                    continue
                # Recurse into neighbor; if cycle is found, bubble up True
                if dfs(neighbor, node):
                    return True

            return False  # No cycle found from this path

        # Process each edge one by one
        for u, v in edges:
            # Add this edge to the graph
            adj_list[u].append(v)
            adj_list[v].append(u)

            # Reset visited array for DFS traversal
            visit = [False] * (n + 1)

            # Run DFS starting from one of the edge's nodes
            if dfs(u, -1):
                # If adding this edge creates a cycle → it's the redundant one
                return [u, v]

        return []  # Fallback (shouldn't reach here for valid inputs)