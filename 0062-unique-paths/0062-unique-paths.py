class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for _ in range(m - 1):
            upper_row = [1] * n
            for i in range(len(upper_row) - 2, -1, -1):
                upper_row[i] = upper_row[i + 1] + row[i]
            row = upper_row
        
        return row[0]
            