class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.upper_left_val = matrix[0][0]
        self.prefix_sum = [[[0, 0] for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                val = matrix[r][c]
                left_sum, upper_square_sum = 0, 0
                if r > 0:
                    upper_square_sum = self.prefix_sum[r - 1][c][1]
                if c > 0:
                    left_sum = self.prefix_sum[r][c - 1][0]

                self.prefix_sum[r][c][0] = val + left_sum
                self.prefix_sum[r][c][1] = val + left_sum + upper_square_sum

                # if r > 0 and c > 0:
                #     self.prefix_sum[r][c] -= self.upper_left_val
        
        for r in self.prefix_sum:
            print(r)
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # upper_left = [row1, col1]
        # upper_right = [row1, col2]
        # lower_left = [row2, col1]
        # lower_right = [row2, col2]

        upper_sum, left_sum = 0, 0
        if row1 - 1 >= 0:
            upper_sum = self.prefix_sum[row1 - 1][col2][1]
        if col1 - 1 >= 0:
            left_sum = self.prefix_sum[row2][col1 - 1][1]
        # print("=============")
        # print(f"upper_left: {row1},{col1}, lower_right: {row2},{col2}, upper_sum: {upper_sum}, left_sum: {left_sum}")
        result = self.prefix_sum[row2][col2][1] - upper_sum - left_sum
        if row1 > 0 and col1 > 0:
            result += self.prefix_sum[row1 - 1][col1 - 1][1]

        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)