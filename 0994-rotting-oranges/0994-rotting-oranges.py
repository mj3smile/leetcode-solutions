class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    rottens.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        result = -1
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        while rottens:
            result += 1
            for _ in range(len(rottens)):
                coord = rottens.popleft()
                r, c = coord

                if coord in visited:
                    continue
                
                visited.add(coord)
                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for n_row, n_col in neighbors:
                    target_row, target_col = r+n_row, c+n_col
                    target_coord = (target_row, target_col)
                    if target_row < 0 or target_row == ROWS or target_col < 0 or target_col == COLS or target_coord in visited or grid[target_row][target_col] != 1:
                        continue
                    
                    grid[target_row][target_col] = 2
                    fresh -= 1
                    rottens.append(target_coord)
        
        if fresh > 0:
            return -1
        return result