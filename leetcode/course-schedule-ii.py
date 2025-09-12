class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list: each course points to its prerequisites
        prereqs = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        output = []       # Stores valid topological order
        visit, cycle = set(), set()  # visited courses & current recursion stack

        # Depth-First Search helper
        def dfs(course):
            # If course is already in recursion stack → cycle detected
            if course in cycle:
                return False
            
            # If already fully processed, skip
            if course in visit:
                return True
            
            # Mark course as being visited in current path
            cycle.add(course)
            # Recursively visit prerequisites
            for prereq in prereqs[course]:
                if dfs(prereq) == False:
                    return False
            
            # Backtrack: remove from recursion stack
            cycle.remove(course)
            # Mark as completed
            visit.add(course)
            # Append to ordering
            output.append(course)
            return True
        
        # Run DFS on all courses
        for c in range(numCourses):
            if dfs(c) == False:
                return []  # Cycle detected, no valid order
        
        return output  # Valid topological ordering