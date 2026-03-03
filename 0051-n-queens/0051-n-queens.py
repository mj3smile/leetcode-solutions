class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.result = list()
        self.generate(list(), set(), set())
        return self.result
    
    def generate(self, combinations, pickedColumn, pickedDiagonal):
        if len(combinations) == self.n:
            self.result.append(combinations.copy())
            return
        
        for col in range(self.n):
            row = len(combinations)
            if self.isSafe(row, col, pickedColumn, pickedDiagonal):
                place = ""
                for j in range(self.n):
                    if j == col:
                        place += "Q"
                    else:
                        place += "."

                pickedColumn.add(col)
                pickedDiagonal.add((row, col))
                combinations.append(place)
                self.generate(combinations, pickedColumn, pickedDiagonal)
                pickedColumn.remove(col)
                pickedDiagonal.remove((row, col))
                combinations.pop()

    
    def isSafe(self, row, col, pickedColumn, pickedDiagonal):
        if col in pickedColumn:
            return False
        
        iteration = 1
        while row - iteration >= 0:
            if (row - iteration, col - iteration) in pickedDiagonal or (row - iteration, col + iteration) in pickedDiagonal:
                return False
            iteration += 1
        
        return True

        
