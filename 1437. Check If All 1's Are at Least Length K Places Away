from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_index = -1 
        
        for i, num in enumerate(nums):
            if num == 1:
                if last_index != -1 and i - last_index <= k:
                    return False
                last_index = i
        return True
