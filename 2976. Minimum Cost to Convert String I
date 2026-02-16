from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        n = 26  
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for o, c, w in zip(original, changed, cost):
            u, v = ord(o) - ord('a'), ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w) 
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]
        
        return total_cost
