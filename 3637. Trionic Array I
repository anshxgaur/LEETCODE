class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        i = 0
        
        # Phase 1: Strictly Increasing (0 to p)
        # Must move at least once to have a valid segment
        has_inc1 = False
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            has_inc1 = True
        
        # Phase 2: Strictly Decreasing (p to q)
        # Must move at least once
        has_dec = False
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
            has_dec = True
            
        # Phase 3: Strictly Increasing (q to n-1)
        # Must move at least once
        has_inc2 = False
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            has_inc2 = True
            
        # We are trionic if we reached the end and all three phases existed
        return i == n - 1 and has_inc1 and has_dec and has_inc2
