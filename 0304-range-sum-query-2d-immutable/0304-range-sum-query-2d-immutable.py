class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = []
        for row in matrix:
            sums = []
            s = 0
            for c in range(len(matrix[0])):
                s += row[c]
                sums.append(s)
            self.sums.append(sums)
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = 0
        for r in range(row1, row2 + 1):
            if col1 == 0:
                sums += self.sums[r][col2]
            else:
                sums = sums + (self.sums[r][col2] - self.sums[r][col1 - 1])
        return sums


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)