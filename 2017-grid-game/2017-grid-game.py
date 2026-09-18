class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        prefix_sum = [[], []]
        postfix_sum = [[0] * len(grid[0]), [0] * len(grid[0])]

        for i in range(len(grid[0])):
            j = len(grid[0]) - 1 - i

            prefix1, prefix2 = grid[0][i], grid[1][i]
            if i > 0:
                prefix1 += prefix_sum[0][-1]
                prefix2 += prefix_sum[1][-1]

            prefix_sum[0].append(prefix1)
            prefix_sum[1].append(prefix2)

            postfix1, postfix2 = grid[0][j], grid[1][j]
            if j < len(grid[0]) - 1:
                postfix1 += postfix_sum[0][j + 1]
                postfix2 += postfix_sum[1][j + 1]
            
            postfix_sum[0][j] = postfix1
            postfix_sum[1][j] = postfix2
        
        result = []
        for c in range(len(grid[0])):
            postfix, prefix = 0, 0
            if c < len(grid[0]) - 1:
                postfix = postfix_sum[0][c + 1]
            if c > 0:
                prefix = prefix_sum[1][c - 1]

            robot2 = max(postfix, prefix)
            if result:
                result[0] = min(result[0], robot2)
            else:
                result.append(robot2)
        
        return result[0]