class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = deque()
        fresh = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                fruit = grid[row][column]

                if fruit == 2:
                    rottens.append((row, column))
                elif fruit == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        minutes = -1
        visited = set()
        while len(rottens) > 0:
            # print("==========")
            # print("rottens", rottens)
            for _ in range(len(rottens)):
                rotten_fruit = rottens.popleft()
                row, column = rotten_fruit[0], rotten_fruit[1]
                
                if grid[row][column] == 1: fresh -= 1
                # print("row:", row, "column:", column, "visited:", visited)
                
                if row > 0 and (row - 1, column) not in visited and grid[row - 1][column] == 1:
                    rottens.append((row - 1, column))
                    visited.add((row - 1, column))
                if row < len(grid) - 1 and (row + 1, column) not in visited and grid[row + 1][column] == 1:
                    rottens.append((row + 1, column))
                    visited.add((row + 1, column))
                if column > 0 and (row, column - 1) not in visited and grid[row][column - 1] == 1:
                    rottens.append((row, column - 1))
                    visited.add((row, column - 1))
                if column < len(grid[0]) - 1 and (row, column + 1) not in visited and grid[row][column + 1] == 1:
                    rottens.append((row, column + 1))
                    visited.add((row, column + 1))
            
            minutes += 1
        
        if fresh > 0:
            return -1
        return minutes