
class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        min_distance = float('inf')
        
        for i, word in enumerate(words):
            if word == target:
                # Calculate circular distance
                dist = min(abs(i - startIndex), n - abs(i - startIndex))
                min_distance = min(min_distance, dist)
        
        return -1 if min_distance == float('inf') else min_distance
