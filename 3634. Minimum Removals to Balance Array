class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Sort the array to ensure the sliding window approach works
        nums.sort()
        
        n = len(nums)
        left = 0
        max_len = 0
        
        # Sliding window
        for right in range(n):
            # While the window is invalid (max > min * k), shrink from the left
            while nums[right] > nums[left] * k:
                left += 1
            
            # Update the maximum number of elements we can keep
            max_len = max(max_len, right - left + 1)
            
        # The result is total elements minus the max elements kept
        return n - max_len
