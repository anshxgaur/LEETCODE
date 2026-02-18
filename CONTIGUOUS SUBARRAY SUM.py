class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder_index = {0: -1}  # remainder -> earliest index
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in remainder_index:
                # Ensure subarray length >= 2
                if i - remainder_index[remainder] > 1:
                    return True
            else:
                # Store the first occurrence of this remainder
                remainder_index[remainder] = i

        return False
