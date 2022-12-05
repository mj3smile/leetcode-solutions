class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        result = list()
        
        def walk(x, y, is_go_up):
            if x < 0 or x >= len(matrix):
                return
            if y < 0 or y >= len(matrix[0]):
                return
            if (x,y) in visited:
                return
            
            visited.add((x,y))
            result.append(matrix[x][y])
            
            if is_go_up:
                walk(x - 1, y, True)
            walk(x, y + 1, False)
            walk(x + 1, y, False)
            walk(x, y - 1, False)
            walk(x - 1, y, True)
        
        walk(0, 0, False)
        return result