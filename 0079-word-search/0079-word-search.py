class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def find(r, c, w):
            if r < 0 or c < 0 or r == len(board) or c == len(board[0]):
                return False
            if board[r][c] != word[w]:
                return False
            if (r, c) in visited:
                return False
            if w == len(word) - 1:
                return True
            
            visited.add((r, c))
            if find(r, c + 1, w + 1):
                return True
            if find(r, c - 1, w + 1):
                return True
            if find(r + 1, c, w + 1):
                return True
            if find(r - 1, c, w + 1):
                return True
            visited.remove((r, c))
            
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if find(r, c, 0):
                    return True
        return False