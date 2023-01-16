class Solution:
    def findInGrid(self, grid, val):
        indexes = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == val:
                    indexes.add((r, c))
        return indexes
                    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])
        queue = deque()
        
        # count fresh orange and find rotten orange
        fresh_orange = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh_orange += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        # count minutes
        minutes = 0
        while queue and fresh_orange > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                directions = {
                    "up": [-1, 0],
                    "left": [0, -1],
                    "down": [1, 0],
                    "right": [0, 1],
                }
                
                for dr, dc in directions.values():
                    r = row + dr
                    c = col + dc
                    
                    if r in range(rowlen) and c in range(collen) and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh_orange -= 1
            
            minutes += 1
        
        return minutes if fresh_orange == 0 else -1