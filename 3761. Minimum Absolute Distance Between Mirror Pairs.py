class Solution(object):
    def minMirrorPairDistance(self, nums):
        def reverse_num(x):
            return int(str(x)[::-1])

        latest_rev = {} 
        min_dist = float('inf')

        for j, num in enumerate(nums):
            if num in latest_rev:
                min_dist = min(min_dist, j - latest_rev[num])
            rev = reverse_num(num)
            latest_rev[rev] = j

        return -1 if min_dist == float('inf') else min_dist
