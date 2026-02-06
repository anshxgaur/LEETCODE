from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n_cols = len(matrix[0])
        heights = [0] * (n_cols + 1)  
        max_area = 0
        
        for row in matrix:
          
            for j in range(n_cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
        
            stack = []
            for i in range(n_cols + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area
