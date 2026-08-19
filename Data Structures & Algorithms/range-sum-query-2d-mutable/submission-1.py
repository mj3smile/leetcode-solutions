class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_sum_row = []
        self.prefix_sum_col = []

        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        for r in range(self.ROWS):
            row = [0 for _ in range(self.COLS)]
            for c in range(self.COLS):
                if c > 0:
                    row[c] = row[c - 1]
                row[c] += matrix[r][c]
            self.prefix_sum_row.append(row)
        
        for c in range(self.COLS):
            col = [0 for _ in range(self.ROWS)]
            for r in range(self.ROWS):
                if r > 0:
                    col[r] = col[r - 1]
                col[r] += matrix[r][c]
            self.prefix_sum_col.append(col)


    def update(self, row: int, col: int, val: int) -> None:
        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS:
            return
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for c in range(col, self.COLS):
            self.prefix_sum_row[row][c] += diff
        for r in range(row, self.ROWS):
            self.prefix_sum_col[col][r] += diff


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        if row2 - row1 < col2 - col1:
            for r in range(row1, row2 + 1):
                t = self.prefix_sum_row[r][col2]
                if col1 > 0:
                    t -= self.prefix_sum_row[r][col1 - 1]
                total += t
        else:
            for c in range(col1, col2 + 1):
                t = self.prefix_sum_col[c][row2]
                if row1 > 0:
                    t -= self.prefix_sum_col[c][row1 - 1]
                print(t)
                total += t
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
