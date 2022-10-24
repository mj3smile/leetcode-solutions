class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowlen = len(board)
        collen = len(board[0])
        visited_coord = set()
        found = False
        
        def find_character(x, y, i):
            if i == len(word):
                nonlocal found
                found = True
                return
            
            if x < 0 or x >= rowlen or y < 0 or y >= collen or (x, y) in visited_coord or board[x][y] != word[i]:
                return
            
            visited_coord.add((x, y))
            find_character(x - 1, y, i + 1)
            find_character(x + 1, y, i + 1)
            find_character(x, y + 1, i + 1)
            find_character(x, y - 1, i + 1)
            visited_coord.remove((x, y))
        
        for x in range(rowlen):
            for y in range(collen):
                if board[x][y] != word[0] or found: continue
                visited_coord = set()
                find_character(x, y, 0)
        
        return found