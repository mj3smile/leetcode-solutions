class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check every row
        for row in board:
            item = set()
            for i in row:
                if i == '.': continue
                if i in item: return False
                item.add(i)
        
        # check every col
        for col in range(len(board[0])):
            item = set()
            for row in range(len(board)):
                if board[row][col] == '.': continue
                if board[row][col] in item: return False
                item.add(board[row][col])
        
        # check every sub-boxes
        boxes = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for box in boxes:
            item = set()
            for r in range(3):
                row = box[0] + r
                for c in range(3):
                    col = box[1] + c
                    if board[row][col] == '.': continue
                    if board[row][col] in item: return False
                    item.add(board[row][col])
        
        return True
                    
                    