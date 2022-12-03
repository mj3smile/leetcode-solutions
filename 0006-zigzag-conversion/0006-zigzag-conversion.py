class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pattern = ["" for _ in range(numRows)]
        
        index = 0
        go_down = True
        for c in s:
            pattern[index] += c
            
            if go_down:
                if index < numRows - 1:
                    index += 1
                else:
                    index -= 1
                    go_down = False
            else:
                if index > 0:
                    index -= 1
                else:
                    index += 1
                    go_down = True
        
        return ''.join(pattern)