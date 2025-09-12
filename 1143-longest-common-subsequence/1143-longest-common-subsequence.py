class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, col = len(text1), len(text2)
        self.dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        for r in range(row):
            for c in range(col):
                if text1[r] == text2[c]:
                    self.dp[r + 1][c + 1] = 1 + self.dp[r][c]
                else:
                    self.dp[r + 1][c + 1] = max(self.dp[r + 1][c], self.dp[r][c + 1])
        
        return self.dp[row][col]