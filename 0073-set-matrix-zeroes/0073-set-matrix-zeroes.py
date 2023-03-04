class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        modified = [[0 for i in range(C)] for j in range(R)]
        
        def modify(row, col):
            for i in range(C):
                if i != col and not modified[row][i] and matrix[row][i] != 0:
                    matrix[row][i] = 0
                    modified[row][i] = 1
            
            for i in range(R):
                if i != row and not modified[i][col] and matrix[i][col] != 0:
                    matrix[i][col] = 0
                    modified[i][col] = 1
        
        for row in range(R):
            for col in range(C):
                if not modified[row][col] and matrix[row][col] == 0:
                    modify(row, col)
        
        
            
            
                
                    
        
        