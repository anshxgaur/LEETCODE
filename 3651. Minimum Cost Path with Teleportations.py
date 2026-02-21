import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18
        
        # dist[i][j][t] = min cost to reach (i,j) using t teleports
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0
        
        # All cells sorted by value (for teleport optimization)
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        
        # For each teleport layer, keep pointer of processed cells
        ptr = [0] * (k + 1)
        
        pq = [(0, 0, 0, 0)]  # cost, i, j, teleports_used
        
        while pq:
            cost, i, j, t = heapq.heappop(pq)
            if cost > dist[i][j][t]:
                continue
            
            # Normal moves
            for ni, nj in ((i + 1, j), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    new_cost = cost + grid[ni][nj]
                    if new_cost < dist[ni][nj][t]:
                        dist[ni][nj][t] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj, t))
            
            # Teleport moves
            if t < k:
                while ptr[t] < len(cells) and cells[ptr[t]][0] <= grid[i][j]:
                    _, x, y = cells[ptr[t]]
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
                    ptr[t] += 1
        
        return min(dist[m - 1][n - 1])
