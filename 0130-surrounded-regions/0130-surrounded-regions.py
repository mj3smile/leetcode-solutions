class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
       
        visited = set()
        def getArea(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] == "X":
                return [], True

            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                return [], False
            
            if (r, c) in visited:
                return [], True
            
            visited.add((r, c))
            surrounded = True
            area = [[r, c]]
            for nr, nc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                a, s = getArea(r + nr, c + nc)
                surrounded = surrounded and s
                area += a

            return area, surrounded
        
        def capture(coords):
            for r, c in coords:
                board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    continue
                
                if (r, c) in visited:
                    continue
                
                area, surrounded = getArea(r, c)
                if surrounded:
                    capture(area)
                

            