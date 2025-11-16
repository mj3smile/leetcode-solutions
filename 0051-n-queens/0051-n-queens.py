class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.result = list()
        for col in range(n):
            self.calcQueenPlace(0, col, list(), set(), set(), set())
        return self.result

    
    def calcQueenPlace(self, row, col, placement, visited_col, visited_diagonal_a, visited_diagonal_b):
        if col in visited_col or row - col in visited_diagonal_a or row + col in visited_diagonal_b:
            return
        
        place_str = ""
        for i in range(self.n):
            char = "."
            if i == col:
                char = "Q"
            place_str += char
        
        placement.append(place_str)
        visited_col.add(col)
        visited_diagonal_a.add(row - col)
        visited_diagonal_b.add(row + col)

        if row < self.n - 1:
            for next_col in range(self.n):
                self.calcQueenPlace(row + 1, next_col, placement, visited_col, visited_diagonal_a, visited_diagonal_b)
        else:
            self.result.append(placement.copy())

        placement.pop()
        visited_col.remove(col)
        visited_diagonal_a.remove(row - col)
        visited_diagonal_b.remove(row + col)