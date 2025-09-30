class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(0 ,0, 1)]) # Append Row, Cols and length it took us to get to this position 
        visited = set((0,0))
        directions = [(1 , 0), (-1 , 0), (0 , 1), (0 , -1) , (1 , 1) , (-1 , -1) , (1 , -1) , (-1 , 1)]

        while q:
            r , c , length = q.popleft()
            if (min(r , c) < 0 or max(r , c) >= n or grid[r][c]):
                continue
            
            if r == n - 1 and c == n - 1:
                return length 
            
            for dr , dc in directions:
                if (r + dr , c + dc) not in visited:
                    q.append((r + dr , c + dc, length + 1))
                    visited.add((r + dr , c + dc))
        
        return -1