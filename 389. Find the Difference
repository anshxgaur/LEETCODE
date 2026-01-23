from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_1=Counter(s)
        freq_2=Counter(t)

        for i in freq_2:
            if freq_2[i]!=freq_1.get(i,0):
                return i
