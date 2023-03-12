class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = []
        for r in range(len(matrix)):
            sums = []
            for c in range(len(matrix[0])):
                s = matrix[r][c]
                if r > 0:
                    s += self.sums[r - 1][c]
                if c > 0:
                    s += sums[c - 1]
                if r > 0 and c > 0:
                    s -= self.sums[r - 1][c - 1]
                sums.append(s)
            self.sums.append(sums)
        print(self.sums)
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.sums[row2][col2]
        if col1 > 0:
            s -= self.sums[row2][col1 -  1]
        if row1 > 0:
            d = self.sums[row1 - 1][col1 - 1] if col1 > 0 else 0
            s -= (self.sums[row1 - 1][col2] - d)
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)