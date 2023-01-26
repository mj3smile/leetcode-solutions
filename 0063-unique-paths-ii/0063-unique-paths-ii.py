class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cols = len(obstacleGrid[0])
        prev_row = [0] * cols
        if obstacleGrid[-1][-1] == 0:
            prev_row[-1] = 1
        
        for r in range(len(obstacleGrid) - 1, -1, -1):
            curr_row = obstacleGrid[r]
            curr_row[-1] = prev_row[-1] if curr_row[-1] == 0 else 0
            for c in range(len(curr_row) - 2, -1, -1):
                if curr_row[c] == 1:
                    curr_row[c] = 0
                else:
                    curr_row[c] = curr_row[c + 1] + prev_row[c]
            prev_row = curr_row
        
        return prev_row[0]