class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        first_char = word[0]

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != first_char:
                    continue
                
                if self.isWordExists(row, col, 0, set()):
                    return True
        
        return False

    def isWordExists(self, row, col, i, cache):
        if i == len(self.word) or row < 0 or row == len(self.board) or col < 0 or col == len(self.board[0]) or self.word[i] != self.board[row][col]:
            return False
        
        if (row, col) in cache:
            return False
        
        if i == len(self.word) - 1:
            return True
        
        cache.add((row, col))
        if (self.isWordExists(row + 1, col, i + 1, cache) or
        self.isWordExists(row, col + 1, i + 1, cache) or
        self.isWordExists(row, col - 1, i + 1, cache) or
        self.isWordExists(row - 1, col, i + 1, cache)):
            return True

        cache.remove((row, col))
        return False