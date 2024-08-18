class Solution:
    def __init__(self):
        self.result = list()
        self.n = 0
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.backtrack('', 0, 0)
        return self.result
    
    def backtrack(self, combination, openCount, closeCount):
        if openCount == closeCount == self.n:
            self.result.append(combination)
            return
        
        if openCount < self.n:
            combination += '('
            self.backtrack(combination, openCount+1, closeCount)
            combination = combination[:len(combination)-1]
        
        if closeCount < openCount:
            combination += ')'
            self.backtrack(combination, openCount, closeCount+1)
        