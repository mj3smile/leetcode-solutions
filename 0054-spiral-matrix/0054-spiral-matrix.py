class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        result = list()

        visited = set()
        def canMoveTo(r, c):
            return r >= 0 and r < ROWS and c >= 0 and c < COLS and (r, c) not in visited

        def trace(r, c, direction):
            # print(r, c)
            result.append(matrix[r][c])
            visited.add((r,c))

            if direction == "right":
                if canMoveTo(r, c + 1):
                    trace(r, c + 1, "right")
                elif canMoveTo(r + 1, c):
                    trace(r + 1, c, "down")
            elif direction == "left":
                if canMoveTo(r, c - 1):
                    trace(r, c - 1, "left")
                elif canMoveTo(r - 1, c):
                    trace(r - 1, c, "up")
            elif direction == "up":
                if canMoveTo(r - 1, c):
                    trace(r - 1, c, "up")
                elif canMoveTo(r, c + 1):
                    trace(r, c + 1, "right")
            else:
                if canMoveTo(r + 1, c):
                    trace(r + 1, c, "down")
                elif canMoveTo(r, c - 1):
                    trace(r, c - 1, "left")
        
        trace(0, 0, "right")
        return result