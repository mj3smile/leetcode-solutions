class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1, numRows + 1):
            row = [1] * i
            for j in range(1, len(row) - 1):
                row[j] = triangle[-1][j - 1] + triangle[-1][j]
            triangle.append(row)
        
        return triangle