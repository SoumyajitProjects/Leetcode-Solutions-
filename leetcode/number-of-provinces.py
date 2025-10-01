from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)       # Total number of cities/nodes
        visited = set()            # Set to track visited cities

        # DFS function to traverse all cities in the same province
        def dfs(i):
            visited.add(i)         # Mark the current city as visited
            for j in range(n):     # Check all other cities
                # If city j is connected to city i and hasn't been visited
                if isConnected[i][j] and j not in visited:
                    dfs(j)         # Recursively visit city j
            return 
        
        provinces = 0              # Count of connected components (provinces)
        for i in range(n):         # Iterate over all cities
            if i not in visited:   # If city i hasn't been visited yet
                provinces += 1     # Found a new province
                dfs(i)             # Visit all cities in this province
        return provinces            # Return total number of provinces