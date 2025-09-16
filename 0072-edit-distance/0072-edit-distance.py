class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for row in range(len(dp)):
            dp[row][-1] = rows - row
        
        for col in range(len(dp[-1])):
            dp[-1][col] = cols - col
        
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if word1[row] == word2[col]:
                    dp[row][col] = dp[row + 1][col + 1]
                else:
                    dp[row][col] = 1 + min(
                        dp[row + 1][col + 1],
                        dp[row][col + 1],
                        dp[row + 1][col]
                    )
        
        return dp[0][0]