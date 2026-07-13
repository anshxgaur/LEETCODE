class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for start in range(1, 10):
            num = 0
            for digit in range(start, 10):
                num = num * 10 + digit
                
                if low <= num <= high:
                    ans.append(num)
                
                if num > high:
                    break
        ans.sort()
        return ans
