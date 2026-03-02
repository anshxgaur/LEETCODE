import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)      # u -> v
        rev_graph = defaultdict(list)  # v -> u

        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))

        dist = [float('inf')] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)

            if cost > dist[u]:
                continue

            # normal edges
            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

            # reversed edges (use switch at u)
            for v, w in rev_graph[u]:
                new_cost = cost + 2 * w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return dist[n - 1] if dist[n - 1] != float('inf') else -1
