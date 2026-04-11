class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        # result = 0

        # def backtrack(row, col, visited):
        #     if row == ROWS or col == COLS or (row, col) in visited or obstacleGrid[row][col] == 1:
        #         return
            
        #     if row == ROWS - 1 and col == COLS - 1:
        #         nonlocal result
        #         result += 1
        #         return
            
        #     visited.add((row, col))
        #     backtrack(row + 1, col, visited)
        #     backtrack(row, col + 1, visited)
        #     visited.remove((row, col))
        
        # backtrack(0, 0, set())
        # return result
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        previousRow = [1 for _ in range(COLS)]
        for i in range(COLS - 1, -1, -1):
            if obstacleGrid[-1][i] == 1:
                previousRow[i] = 0
            elif i + 1 < COLS:
                previousRow[i] = previousRow[i + 1]
        
        for r in range(ROWS - 2, -1, -1):
            currentRow = [0 for _ in range(COLS)]
            if obstacleGrid[r][-1] == 1:
                currentRow[-1] = 0
            else:
                currentRow[-1] = previousRow[-1]

            for c in range(len(currentRow) - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    currentRow[c] = 0
                else:
                    currentRow[c] = currentRow[c + 1] + previousRow[c]
            
            previousRow = currentRow
        
        return previousRow[0]
