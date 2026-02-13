class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def wordExist(row, col, targetIndex, visited):
            if targetIndex == len(word):
                return True

            if row < 0 or row == rows or col < 0 or col == cols or board[row][col] != word[targetIndex] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            result = (
                wordExist(row+1, col, targetIndex+1, visited) or
                wordExist(row-1, col, targetIndex+1, visited) or
                wordExist(row, col+1, targetIndex+1, visited) or
                wordExist(row, col-1, targetIndex+1, visited)
            )
            visited.remove((row, col))
            return True and result
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if wordExist(r, c, 0, set()):
                    return True
        
        return False
            