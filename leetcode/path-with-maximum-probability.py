from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Step 1: Build adjacency list
        # Each node maps to a list of tuples (neighbor, success probability)
        adj_list = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]           # Edge from a -> b
            val = succProb[i]         # Success probability of that edge
            adj_list[a].append((b, val))
            adj_list[b].append((a, val))  # Since undirected graph

        # Step 2: Initialize max-heap for Dijkstra-style traversal
        # We use negative probabilities because heapq in Python is a min-heap
        # By pushing negative, the largest probability comes first
        pq = [(-1, start_node)]  # (-probability, node)
        visited = set()          # Track nodes we've already finalized

        # Step 3: Main loop: process nodes from heap
        while pq:
            prob, node = heapq.heappop(pq)  # Get node with current max probability
            visited.add(node)                # Mark this node as visited

            # Step 4: If we reached the target node, return probability
            if node == end_node:
                return prob * -1             # Multiply by -1 to get positive probability

            # Step 5: Explore neighbors
            for nei, edge_prob in adj_list[node]:
                if nei not in visited:
                    # Multiply probability along the path
                    # Push negative probability to maintain max-heap property
                    heapq.heappush(pq, (prob * edge_prob, nei))

        # Step 6: If end_node is not reachable, return 0.0
        return 0.0