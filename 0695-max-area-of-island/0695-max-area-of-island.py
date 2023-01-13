class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        visited = set()
        
        def dfs(r, c):
            rowlen, collen = len(grid), len(grid[0])
            if min(r, c) < 0 or r == rowlen or c == collen or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            land = 1
            land += dfs(r, c + 1)
            land += dfs(r, c - 1)
            land += dfs(r + 1, c)
            land += dfs(r - 1, c)
            
            return land
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                result = max(result, dfs(r, c))
        
        return result