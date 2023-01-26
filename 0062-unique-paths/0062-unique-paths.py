class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n
        
        for _ in range(m - 1):
            curr_row = [1] * n
            for i in range(len(curr_row) - 2, -1, -1):
                curr_row[i] = curr_row[i + 1] + prev_row[i]
            prev_row = curr_row
        
        return prev_row[0]
            