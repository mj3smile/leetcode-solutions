class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[1])):
                val = board[r][c]
                if val == '.': continue
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[(r // 3, c // 3)]): return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
                
        return True