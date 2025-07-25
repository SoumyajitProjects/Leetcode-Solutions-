class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build an adjacency list representing prerequisites for each course
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()  # Tracks the current DFS path to detect cycles

        # Depth-First Search to detect cycles
        def dfs(crs):
            # If course is already in the current DFS path, a cycle is detected
            if crs in visitSet:
                return False

            # If no prerequisites, course can be completed
            if preMap[crs] == []:
                return True

            # Mark current course as being visited
            visitSet.add(crs)

            # Visit all prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # After visiting, remove from path and mark course as completed
            visitSet.remove(crs)
            preMap[crs] = []  # Memoize: mark as no prerequisites
            return True

        # Run DFS on every course
        for crs in range(numCourses):
            if not dfs(crs):
                return False  # A cycle was found

        return True  # All courses can be finished