from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_prefix = [[0]*(n+1) for _ in range(m)]
        col_prefix = [[0]*(m+1) for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                row_prefix[i][j+1] = row_prefix[i][j] + grid[i][j]
                col_prefix[j][i+1] = col_prefix[j][i] + grid[i][j]
        
        def check(r, c, k):
            target = None
            
            for i in range(r, r+k):
                row_sum = row_prefix[i][c+k] - row_prefix[i][c]
                if target is None:
                    target = row_sum
                elif target != row_sum:
                    return False
        
            for j in range(c, c+k):
                col_sum = col_prefix[j][r+k] - col_prefix[j][r]
                if target != col_sum:
                    return False
            
            diag1 = sum(grid[r+i][c+i] for i in range(k))
            diag2 = sum(grid[r+i][c+k-1-i] for i in range(k))
            if target != diag1 or target != diag2:
                return False
            
            return True
        
        for k in range(min(m, n), 0, -1):
            for r in range(m-k+1):
                for c in range(n-k+1):
                    if check(r, c, k):
                        return k
        return 1
