class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        modified = [[0 for i in range(C)] for j in range(R)]
        
        def modify(row, col):
            print(row, col)
            for i in range(1, C + 1):
                left, right = col - i, col + i
                if left >= 0 and not modified[row][left] and matrix[row][left] != 0:
                    matrix[row][left] = 0
                    modified[row][left] = 1
                
                if right < C and not modified[row][right] and matrix[row][right] != 0:
                    matrix[row][right] = 0
                    modified[row][right] = 1
            
            for i in range(1, R + 1):
                up, down = row - i, row + i
                if up >= 0 and not modified[up][col] and matrix[up][col] != 0:
                    matrix[up][col] = 0
                    modified[up][col] = 1
                
                if down < R and not modified[down][col] and matrix[down][col] != 0:
                    matrix[down][col] = 0
                    modified[down][col] = 1
        
        for row in range(R):
            for col in range(C):
                if not modified[row][col] and matrix[row][col] == 0:
                    modify(row, col)
        
        
            
            
                
                    
        
        