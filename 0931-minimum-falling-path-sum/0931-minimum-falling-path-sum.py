class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in range(len(matrix) - 2, -1, -1):
            for c in range(len(matrix[r])):
                chosen = matrix[r + 1][c]
                if c > 0:
                    chosen = min(chosen, matrix[r + 1][c - 1])
                if c < len(matrix) - 1:
                    chosen = min(chosen, matrix[r + 1][c + 1])
                
                matrix[r][c] += chosen
        
        result = matrix[0][0]
        for v in matrix[0]:
            result = min(result, v)
        
        return result