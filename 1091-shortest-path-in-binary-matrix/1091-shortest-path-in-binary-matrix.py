class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowlen = collen = len(grid)
        queue = deque()
        visited = set()
        if grid[0][0] == 0:
            queue.append((0, 0))
            visited.add((0, 0))
        
        length = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == rowlen - 1 and col == collen - 1:
                    return length + 1
                
                directions = {
                    "up": [-1, 0],
                    "upright": [-1, 1],
                    "right": [0, 1],
                    "downright": [1, 1],
                    "down": [1, 0],
                    "downleft": [1, -1],
                    "left": [0, -1],
                    "upleft": [-1, -1]
                }
                
                for dr, dc in directions.values():
                    r = row - dr
                    c = col - dc
                    if min(r, c) < 0 or r == rowlen or c == collen or grid[r][c] == 1 or (r, c) in visited:
                        continue
                    queue.append((r, c))
                    visited.add((r, c))
            length += 1
        
        return -1