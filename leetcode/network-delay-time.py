class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # First create adjaceny list:
        adj_list = {i: [] for i in range(1 , n + 1)}

        for u , v , t in times:
            adj_list[u].append((v , t)) # u -> v with time t
        
        # Use Dijkstra's algorithm to find shortest path from node k (source node)
        pq = [(0 , k)]
        dist = {i: float('inf') for i in range(1 , n + 1)} # Distance to each node
        dist[k] = 0

        while pq:
            # Get the node with the minimun time
            time , node  = heapq.heappop(pq)

            # If we already found a shorter path then skip the process:

            if time > dist[node]:
                continue
            
            for nei , edge_time in adj_list[node]:
                new_time = time + edge_time
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time , nei))
        
        max_time = max(dist.values())
        return max_time if max_time < float('inf') else -1