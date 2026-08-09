class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def countRowScoreByOne(r):
            score = 0
            n = COLS - 1
            for i in range(len(grid[r]) - 1, -1, -1):
                if grid[r][i] == 0:
                    continue
                score += (2**(n - i))
            return score
        
        def countRowScoreByZero(r):
            score = 0
            n = COLS - 1
            for i in range(len(grid[r]) - 1, -1, -1):
                if grid[r][i] == 1:
                    continue
                score += (2**(n - i))
            return score
        
        def countColumnZeroAndOne(c):
            zero, one = 0, 0
            for r in range(ROWS):
                if grid[r][c] == 0:
                    zero += 1
                else:
                    one += 1
            return zero, one
        
        def countScore():
            score = 0
            for r in range(ROWS):
                score += countRowScoreByOne(r)
            return score
        
        def flip(n):
            if n == 0:
                return 1
            return 0

        for r in range(ROWS):
            before = countRowScoreByOne(r)
            after = countRowScoreByZero(r)

            if after > before:
                for c in range(COLS):
                    grid[r][c] = flip(grid[r][c])
        
        for c in range(COLS):
            zero, one = countColumnZeroAndOne(c)
            if zero > one:
                for r in range(ROWS):
                    grid[r][c] = flip(grid[r][c])
        
        return countScore()