class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(i):
            visited.add(i)
            for key in rooms[i]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        return len(visited) == n