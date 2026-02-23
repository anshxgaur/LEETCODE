class Solution(object):
    def numPairsDivisibleBy60(self, time):
        from collections import defaultdict
        
        count = defaultdict(int)
        result = 0
        
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60
            result += count[complement]
            count[remainder] += 1
        
        return result
