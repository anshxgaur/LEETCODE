from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
     
        total = 0.0
        lo = float('inf')
        hi = float('-inf')
        for x, y, l in squares:
            total += l * l
            lo = min(lo, y)
            hi = max(hi, y + l)
        
        target = total / 2.0
        
        def above_area(y: float) -> float:
            s = 0.0
            for _, yi, li in squares:
                top = yi + li
                if y <= yi:
                    s += li * li
                elif y >= top:
                    continue
                else:
                    s += (top - y) * li
            return s  
        for _ in range(70):
            mid = (lo + hi) / 2.0
            if above_area(mid) > target:
                lo = mid
            else:
                hi = mid
        
        return (lo + hi) / 2.0
