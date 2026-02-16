from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Find the minimum difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            min_diff = min(min_diff, diff)
        
        # Step 3: Collect all pairs with min_diff
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])
        
        return result
