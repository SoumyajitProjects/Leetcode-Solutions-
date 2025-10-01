import heapq
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        ROWS, COLS = len(mat), len(mat[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Correctly initialize distance matrix
        dist = [[float('inf')] * COLS for _ in range(ROWS)]

        min_heap = []

        # Push all 0 cells into heap
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    heapq.heappush(min_heap, (0, r, c))

        # Dijkstra / BFS
        while min_heap:
            d, r, c = heapq.heappop(min_heap)

            # Skip if we already found a shorter path
            if d > dist[r][c]:
                continue

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < ROWS and 0 <= newC < COLS:
                    new_dist = d + 1
                    if new_dist < dist[newR][newC]:
                        dist[newR][newC] = new_dist
                        heapq.heappush(min_heap, (new_dist, newR, newC))

        return dist