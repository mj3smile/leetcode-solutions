class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        servers_in_row = dict()
        servers_in_col = dict()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    servers_in_row[r] = servers_in_row.get(r, 0) + 1
                    servers_in_col[c] = servers_in_col.get(c, 0) + 1
        
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (servers_in_row.get(r, 0) > 1 or servers_in_col.get(c, 0) > 1):
                    result += 1
        
        return result