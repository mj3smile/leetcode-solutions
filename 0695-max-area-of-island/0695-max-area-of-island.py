class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.result = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1:
                    # print("before",self.grid)
                    self.countAreaOfIsland(r, c, [0])
                    # print("after",self.grid)
                    # print("result:", self.result)

        return self.result

    def countAreaOfIsland(self, row, col, area):
        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.grid[row][col] == 0:
            return
        
        self.grid[row][col] = 0
        area[0] += 1
        self.result = max(self.result, area[0])

        for r, c in [[0,1],[0,-1],[1,0],[-1,0]]:
            self.countAreaOfIsland(row + r, col + c, area)