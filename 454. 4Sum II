class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):

        from collections import defaultdict

        count = defaultdict(int)
        for a in nums1:
            for b in nums2:
                count[a + b] += 1

        result = 0
        for c in nums3:
            for d in nums4:
                result += count[-(c + d)]

        return result
