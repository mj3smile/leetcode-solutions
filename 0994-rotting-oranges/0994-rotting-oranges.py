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
        visited = set()
        queue = deque()
        
        # find rotten
        fresh_orange = self.findInGrid(grid, 1)
        if not fresh_orange: return 0
        for i in self.findInGrid(grid, 2):
            queue.append(i)
            visited.add(i)
        
        # bfs
        result = -1
        while queue:
            # print(queue)
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
                    
                    if min(r, c) < 0 or r == rowlen or c == collen or (r, c) in visited or grid[r][c] != 1:
                        continue
                    
                    grid[r][c] = 2
                    queue.append((r, c))
                    visited.add((r, c))
                    fresh_orange.remove((r, c))
            
            result += 1
        
        return result if not fresh_orange else -1