class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def word_to_num(word: str) -> int:
            num_str = ''.join(str(ord(ch) - ord('a')) for ch in word)
            return int(num_str)
        
        return word_to_num(firstWord) + word_to_num(secondWord) == word_to_num(targetWord)
