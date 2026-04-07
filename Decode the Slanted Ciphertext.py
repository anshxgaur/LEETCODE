

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Calculate the number of columns in the grid
        cols = len(encodedText) // rows
        
        decoded_chars = []
        
        # Traverse starting from each column in the first row
        for start_col in range(cols):
            r = 0
            c = start_col
            
            # Move diagonally down-right
            while r < rows and c < cols:
                # Map 2D coordinates (r, c) to the 1D index of encodedText
                idx = r * cols + c
                decoded_chars.append(encodedText[idx])
                
                r += 1
                c += 1
                
        # Join the characters and remove trailing spaces
        return "".join(decoded_chars).rstrip()
