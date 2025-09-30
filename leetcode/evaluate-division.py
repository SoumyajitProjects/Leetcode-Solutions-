from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        for i in range(len(equations)):
            num , den = equations[i]
            val = values[i]
            adj_list[num].append((den, val))
            adj_list[den].append((num, 1.0/val))
        
        res = []

        def dfs(node, prod, den, visited):
            visited.add(node)
            if node == den:
                return prod
            for nei, val in adj_list[node]:
                if nei in visited:
                    continue
                new_prod = prod * val
                res = dfs(nei, new_prod, den, visited)
                if res != -1.0:
                    return res
            return -1.0

        for num, den in queries:
            if num not in adj_list or den not in adj_list:
                res.append(-1.0)
            else:
                product = dfs(num, 1, den, set())
                res.append(product)

        return res