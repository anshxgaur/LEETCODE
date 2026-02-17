from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        # We need to pick k-1 more elements from a window of size dist + 1
        # The first element nums[0] is always included.
        # The window size for the remaining k-1 elements is dist + 1.
        
        target_count = k - 1
        window_size = dist + 1
        
        # left maintains the smallest target_count elements
        left = SortedList()
        # right maintains the rest of the elements in the current window
        right = SortedList()
        
        current_sum = 0
        
        def add(val):
            nonlocal current_sum
            left.add(val)
            current_sum += val
            # If left grows too large, move the largest to right
            if len(left) > target_count:
                max_val = left.pop()
                current_sum -= max_val
                right.add(max_val)
                
        def remove(val):
            nonlocal current_sum
            if val in left:
                left.remove(val)
                current_sum -= val
                # Refill left from right if possible
                if right:
                    min_val = right.pop(0)
                    current_sum += min_val
                    left.add(min_val)
            else:
                right.remove(val)

        # Initial window from index 1 to window_size
        for i in range(1, min(window_size + 1, n)):
            add(nums[i])
            
        min_total_cost = nums[0] + current_sum
        
        # Slide the window across the rest of the array
        for i in range(window_size + 1, n):
            # Remove the element that fell out of the window (nums[i - window_size])
            remove(nums[i - window_size])
            # Add the new element
            add(nums[i])
            # Update result
            min_total_cost = min(min_total_cost, nums[0] + current_sum)
            
        return min_total_cost
