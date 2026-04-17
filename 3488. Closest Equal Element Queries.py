
from collections import defaultdict
class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        val_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            val_to_indices[num].append(i)
        closest = [-1] * n
        for indices in val_to_indices.values():
            k_len = len(indices)
            if k_len <= 1:
                continue
                
            for k in range(k_len):
                i = indices[k]
                prev_i = indices[(k - 1) % k_len]
                next_i = indices[(k + 1) % k_len]
                dist_prev = abs(i - prev_i)
                dist_prev = min(dist_prev, n - dist_prev)
                
                dist_next = abs(i - next_i)
                dist_next = min(dist_next, n - dist_next)
                closest[i] = min(dist_prev, dist_next)
        return [closest[q] for q in queries]
