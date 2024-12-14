class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_cache = dict()
        board_cache  = dict()
        
        for r in range(len(board)):
            row = r + 1
            row_cache = set()

            for c in range(len(board[r])):
                val = board[r][c]
                if val == ".":
                    continue
                    
                col     = c + 1
                board_n = self.getBoard(row, col)
                column_cache[col]    = column_cache.get(col, set())
                board_cache[board_n] = board_cache.get(board_n, set())
                
                if val in row_cache or val in column_cache[col] or val in board_cache[board_n]:
                    return False
                
                row_cache.add(val)
                column_cache[col].add(val)
                board_cache[board_n].add(val)
        
        return True
    
    def getBoard(self, row: int, column: int) -> int:
        if row in {1, 2, 3}:
            if column in {1, 2, 3}:
                return 1
            elif column in {4, 5, 6}:
                return 2
            elif column in {7, 8, 9}:
                return 3
        if row in {4, 5, 6}:
            if column in {1, 2, 3}:
                return 4
            elif column in {4, 5, 6}:
                return 5
            elif column in {7, 8, 9}:
                return 6
        if row in {7, 8, 9}:
            if column in {1, 2, 3}:
                return 7
            elif column in {4, 5, 6}:
                return 8
            elif column in {7, 8, 9}:
                return 9