class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        
        def dfs(r, c):
            rowlen, collen = len(grid), len(grid[0])
            if min(r, c) < 0 or r == rowlen or c == collen or grid[r][c] == "0" or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
            
            return 1
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                islands += dfs(r, c)
        
        return islands
            