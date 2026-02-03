class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        def oceanReached(r, c, visited):
            reached = set()
            result = 0
            if (r == 0 and c == COLS - 1) or (c == 0 and r == ROWS - 1) or (r == 0 and r == ROWS - 1) or (c == 0 and c == COLS - 1):
                return 3
            elif r == 0 or c == 0:
                reached.add(1)
                result += 1
            elif r == ROWS - 1 or c == COLS - 1:
                reached.add(2)
                result += 2

            neighbor = [[0,1],[0,-1],[1,0],[-1,0]]
            visited.add((r, c))
            for n_row, n_col in neighbor:
                target_r, target_c = n_row + r, n_col + c
                if target_r < 0 or target_r == ROWS or target_c < 0 or target_c == COLS or heights[target_r][target_c] > heights[r][c] or (target_r, target_c) in visited:
                    continue

                o = oceanReached(target_r, target_c, visited)
                if o in reached:
                    continue
                if o == 3:
                    result = 3
                    break
                reached.add(o)
                result += o

            visited.remove((r, c))
            return result
        
        result = list()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if oceanReached(r, c, set()) == 3:
                    result.append([r, c])
        
        return result