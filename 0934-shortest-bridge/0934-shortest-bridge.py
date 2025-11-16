class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid

        first_island_row, first_island_col = 0, 0
        for r in range(self.rows):
            found = False
            for c in range(self.cols):
                if grid[r][c] == 1:
                    found = True
                    first_island_row = r
                    first_island_col = c
                    break
            if found: break
        
        self.queue = deque()
        self.visited = set()
        self.calcFirstIslandLands(first_island_row, first_island_col)

        # print("queue:", self.queue, first_island_row, first_island_col)
        result = 0
        visited = set()
        while self.queue:
            # print("queue:", self.queue)
            for _ in range(len(self.queue)):
                coord = self.queue.popleft()
                row, col = coord
                
                # if coord not in self.visited and grid[row][col] == 1:
                #     return result
                
                # self.visited.add(coord)
                for nr, nc in [[1,0],[-1,0],[0,-1],[0,1]]:
                    new_row, new_col = row + nr, col + nc
                    # print(new_row, new_col)
                    if new_row < 0 or new_row == self.rows or new_col < 0 or new_col == self.cols or (new_row, new_col) in self.visited:
                        continue
                    if grid[new_row][new_col] == 1:
                        return result
                    # print("here")
                    self.visited.add((new_row, new_col))
                    self.queue.append((new_row, new_col))
                
            result += 1
        
        return result

    def calcFirstIslandLands(self, row, col):
        if row < 0 or row == self.rows or col < 0 or col == self.cols or (row, col) in self.visited or self.grid[row][col] == 0:
            return
        
        self.queue.append((row, col))
        self.visited.add((row, col))
        self.calcFirstIslandLands(row + 1, col)
        self.calcFirstIslandLands(row - 1, col)
        self.calcFirstIslandLands(row, col + 1)
        self.calcFirstIslandLands(row, col - 1)