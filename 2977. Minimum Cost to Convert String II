from typing import List
import math

class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str], cost: List[int]) -> int:

        n = len(source)
        INF = 10**18

        # Group transformations by length
        by_len = {}
        for o, c, w in zip(original, changed, cost):
            L = len(o)
            if L not in by_len:
                by_len[L] = {}
            if o not in by_len[L]:
                by_len[L][o] = {}
            by_len[L][o][c] = min(by_len[L][o].get(c, INF), w)

        # Floyd-Warshall for each length
        min_cost = {}
        for L, mp in by_len.items():
            nodes = set(mp.keys())
            for u in mp:
                nodes.update(mp[u].keys())

            nodes = list(nodes)
            idx = {s: i for i, s in enumerate(nodes)}
            m = len(nodes)

            dist = [[INF] * m for _ in range(m)]
            for i in range(m):
                dist[i][i] = 0

            for u in mp:
                for v in mp[u]:
                    dist[idx[u]][idx[v]] = min(dist[idx[u]][idx[v]], mp[u][v])

            for k in range(m):
                for i in range(m):
                    for j in range(m):
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]

            min_cost[L] = (nodes, idx, dist)

        # DP
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            # Case 1: single character match
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            # Case 2: substring transformations
            for L in min_cost:
                if i + L > n:
                    continue
                s = source[i:i + L]
                t = target[i:i + L]
                nodes, idx, dist = min_cost[L]
                if s in idx and t in idx:
                    c = dist[idx[s]][idx[t]]
                    if c < INF:
                        dp[i] = min(dp[i], c + dp[i + L])

        return -1 if dp[0] >= INF else dp[0]
