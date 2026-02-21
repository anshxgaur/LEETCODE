class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        # Use a sufficiently small number for invalid states
        NEG_INF = -float('inf')
        
        # These variables store the max sum of a valid phase ENDING at index i-1
        # prev_inc1: Strictly Increasing (length >= 2)
        # prev_dec:  Strictly Increasing -> Strictly Decreasing
        # prev_inc2: Strictly Increasing -> Strictly Decreasing -> Strictly Increasing
        prev_inc1 = NEG_INF
        prev_dec = NEG_INF
        prev_inc2 = NEG_INF
        
        ans = NEG_INF
        
        for i in range(1, n):
            # Calculate current states ending at i based on previous states
            curr_inc1 = NEG_INF
            curr_dec = NEG_INF
            curr_inc2 = NEG_INF
            
            # --- PHASE 1: Strictly Increasing (l...p) ---
            if nums[i] > nums[i-1]:
                # Option A: Extend an existing increasing sequence
                # Option B: Start a new increasing sequence with [nums[i-1], nums[i]]
                # max(prev_inc1, nums[i-1]) ensures we pick the better start
                curr_inc1 = max(prev_inc1, nums[i-1]) + nums[i]

            # --- PHASE 2: Strictly Decreasing (p...q) ---
            if nums[i] < nums[i-1]:
                # Option A: Transition from a valid Phase 1
                if prev_inc1 != NEG_INF:
                    curr_dec = max(curr_dec, prev_inc1 + nums[i])
                # Option B: Extend an existing decreasing sequence
                if prev_dec != NEG_INF:
                    curr_dec = max(curr_dec, prev_dec + nums[i])
                    
            # --- PHASE 3: Strictly Increasing (q...r) ---
            if nums[i] > nums[i-1]:
                # Option A: Transition from a valid Phase 2
                if prev_dec != NEG_INF:
                    curr_inc2 = max(curr_inc2, prev_dec + nums[i])
                # Option B: Extend an existing Phase 3
                if prev_inc2 != NEG_INF:
                    curr_inc2 = max(curr_inc2, prev_inc2 + nums[i])

            # Update global max answer if we have a valid Phase 3 ending here
            if curr_inc2 != NEG_INF:
                ans = max(ans, curr_inc2)
            
            # Move current states to previous for next iteration
            prev_inc1 = curr_inc1
            prev_dec = curr_dec
            prev_inc2 = curr_inc2
            
        return int(ans)
