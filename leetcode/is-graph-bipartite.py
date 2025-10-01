from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)                   # Number of nodes in the graph
        color = [0] * n                  # 0 = unvisited, 1 = color A, -1 = color B

        # Iterate over all nodes to handle disconnected graphs
        for i in range(n):
            if color[i] != 0:            # Skip already visited/colored nodes
                continue

            # Start BFS from node i
            queue = deque([i])
            color[i] = 1                 # Assign first color

            while queue:
                node = queue.popleft()   # Get the current node
                for neighbor in graph[node]:  # Check all neighbors
                    if color[neighbor] == 0:
                        # If neighbor is unvisited, color it with opposite color
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # If neighbor has same color, graph is not bipartite
                        return False
        # If BFS completes without conflicts, the graph is bipartite
        return True