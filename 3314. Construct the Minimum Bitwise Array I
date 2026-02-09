from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
                continue
            r = 0
            t = num
            while t & 1:
                r += 1
                t >>= 1
            ans.append(num - (1 << (r - 1)))
        return ans
