class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        num &= 0xffffffff
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            digit = num & 0xf  
            result.append(hex_chars[digit])
            num >>= 4         
        
        return "".join(reversed(result))
