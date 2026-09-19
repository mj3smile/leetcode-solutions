class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = list()
        for _ in range(numRows):
            zigzag.append(list())
        
        def getNextIndex(r, c, direction):
            next_r, next_c, next_direction = r, c, direction
            if direction == "down":
                if r == numRows - 1:
                    next_r = max(0, r - 1)
                    next_c = c + 1
                else:
                    next_r = min(numRows - 1, r + 1)
            elif direction == "up":
                if r == 0:
                    next_r = min(numRows - 1, r + 1)
                    next_c = c
                else:
                    next_r = max(0, r - 1)
                    next_c = c + 1
            if next_r == 0:
                next_direction = "down"
            elif next_r == numRows - 1:
                next_direction = "up"
                
            return next_r, next_c, next_direction
        
        next_r, next_c, next_direction = 0, 0, "down"
        for char in s:
            while len(zigzag[next_r]) < next_c + 1:
                zigzag[next_r].append("")
            zigzag[next_r][next_c] = char
            next_r, next_c, next_direction = getNextIndex(next_r, next_c, next_direction)
            print(char, next_r, next_c, next_direction)
        
        result = ""
        for r in zigzag:
            result += "".join(r)
        
        return result
