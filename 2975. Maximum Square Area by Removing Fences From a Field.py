from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        hFences = [1] + sorted(hFences) + [m]
        vFences = [1] + sorted(vFences) + [n]
        
        vdiffs = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                vdiffs.add(vFences[j] - vFences[i])
        
        best = 0
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                d = hFences[j] - hFences[i]
                if d in vdiffs:
                    best = max(best, d)
        
       
        if best == 0:
            return -1
        
        return (best * best) % MOD
