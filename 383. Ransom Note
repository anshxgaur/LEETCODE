

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = defaultdict(int)
        magzine = defaultdict(int)

        for ch in magazine:
            magzine[ch] += 1

        for ch in ransomNote:
            ransom[ch] += 1

        for ch in ransom:
            if ransom[ch] > magzine.get(ch, 0):
                return False
        return True
