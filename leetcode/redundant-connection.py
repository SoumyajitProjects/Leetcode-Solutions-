class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = {i: [] for i in range(1, n + 1)}

        def dfs(node, parent, visited):
            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    if dfs(nei, node, visited):
                        return True
                
                elif nei != parent:
                    return True
            
            return False
        
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

            visited = set()
            if dfs(u , -1, visited):
                return [u, v]
        
        return []