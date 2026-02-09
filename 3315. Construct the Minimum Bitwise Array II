from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
                continue

            t = 0
            while (num >> t) & 1:
                t += 1

            ans.append(num - (1 << (t - 1)))
        return ans
