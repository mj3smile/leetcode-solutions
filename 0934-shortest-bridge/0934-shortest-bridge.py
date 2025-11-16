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
        self.calcFirstIslandLands(0, 0, first_island_row, first_island_col, set())

        result = 0
        while self.queue:
            for _ in range(len(self.queue)):
                coord = self.queue.popleft()
                row, col = coord
                for r, c in [[1,0],[-1,0],[0,-1],[0,1]]:
                    new_row, new_col = row + r, col + c
                    if new_row < 0 or new_row == self.rows or new_col < 0 or new_col == self.cols or (new_row, new_col) in self.visited:
                        continue
                    if grid[new_row][new_col] == 1:
                        return result
                    
                    self.visited.add((new_row, new_col))
                    self.queue.append((new_row, new_col))
                
            result += 1
        
        return result

    def calcFirstIslandLands(self, prev_row, prev_col, row, col, cache):
        if row < 0 or row == self.rows or col < 0 or col == self.cols or (row, col) in self.visited:
            return
        
        if self.grid[row][col] == 0:
            key = (prev_row, prev_col)
            if key in cache:
                return
            cache.add(key)
            self.queue.append(key)
            return
        
        self.visited.add((row, col))
        for r, c in [[1,0],[-1,0],[0,-1],[0,1]]:
            self.calcFirstIslandLands(row, col, row + r, col + c, cache)