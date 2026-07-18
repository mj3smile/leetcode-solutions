class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                next_i, next_j = i, j + k
                while next_j >= len(grid[i]):
                    next_i += 1
                    next_j = next_j - len(grid[i])
                    if next_i == len(grid):
                        next_i = 0
                
                result[next_i][next_j] = grid[i][j]
        
        return result