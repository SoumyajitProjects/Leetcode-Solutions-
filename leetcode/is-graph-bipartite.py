from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # 0: unvisited, 1: color A, -1: color B

        for i in range(n):
            if color[i] != 0:
                continue  # Already colored, skip

            queue = deque([i])
            color[i] = 1  # Start with color 1

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]  # Alternate color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False  # Same color on both sides? Not bipartite
        return True