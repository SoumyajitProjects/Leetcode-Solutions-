class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for s , d , p in flights:
            adj_list[s].append((d , p))
        
        q = deque([(0 , src , 0)])
        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            cost , node, stops = q.popleft()

            if stops > k:
                continue
            
            for nei, edge_price in adj_list[node]:
                new_cost = cost + edge_price
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    q.append((new_cost , nei , stops + 1))
        
        return dist[dst] if dist[dst] != float('inf') else -1