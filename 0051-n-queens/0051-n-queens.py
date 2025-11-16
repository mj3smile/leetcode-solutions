class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.result = list()
        # result = list()

        # limit = n // 2
        # if n % 2 > 0:
        #     limit += 1

        # for first_queen_placement in range(limit):
        #     self.prohibited = set()
        #     self.queens_place = [[], []]
        #     self.placeIn(0, first_queen_placement)
        #     finished = True

        #     for queen in range(1, self.n):
        #         row = queen
        #         ok, col = self.canFindColBoard(row)
        #         if not ok:
        #             finished = False
        #             break

        #         self.placeIn(row, col)
            
        #     if finished:
        #         result.append(self.queens_place[0])
        #         if self.queens_place[1]: result.append(self.queens_place[1])
        
        # return result
        for col in range(n):
            self.calcQueenPlace(0, col, list(), set(), set(), set(), set())
        return self.result

    
    def canFindColBoard(self, board_row):
        # found, col = False, 0
        
        for c in range(self.n):
            if (board_row, c) not in self.prohibited:
                # found = True
                # col = c
                # break
                return True, c
        
        return False, 0
        # if not found:
            # print("queenss:", board_row)
            # return False, 0
        
        # if board_row == 1:
        #     print("prohibited for queen 1:", self.prohibited)
        #     print("found:", board_row, col)
            # print((board_row, ))

        # self.placeIn(board_row, col)
        # return True, col
    
    def placeIn(self, board_row, col):
        diagonal_right = col + 1
        diagonal_left = col - 1
        for row in range(board_row + 1, self.n):
            self.prohibited.add((row, col))
            if diagonal_right >= 0 and diagonal_right < self.n:
                self.prohibited.add((row, diagonal_right))
            if diagonal_left >= 0 and diagonal_left < self.n:
                self.prohibited.add((row, diagonal_left))
            diagonal_right += 1
            diagonal_left -= 1
        
        placement1, placement2 = "", ""
        for i in range(self.n):
            char = "."
            if i == col:
                char = "Q"

            placement1 += char
            placement2 = char + placement2
        
        self.queens_place[0].append(placement1)
        if placement1 != placement2:
            self.queens_place[1].append(placement2)

        # self.queens_place.append((board_row, col))
    
    def calcQueenPlace(self, row, col, placement, visited_col, visited_diagonal_a, visited_diagonal_b, cache):
        if row == self.n:
            cache_key = "".join(placement)
            if cache_key in cache:
                return
                # print("0,1 visited col", visited_col)
            self.result.append(placement.copy())
            cache.add(cache_key)
            return
        
        if col in visited_col or row - col in visited_diagonal_a or row + col in visited_diagonal_b:
            return
        
        # if row == 0 and col == 1:
        #     print("0,1 visited col", visited_col)

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
        for next_col in range(self.n):
            self.calcQueenPlace(row + 1, next_col, placement, visited_col, visited_diagonal_a, visited_diagonal_b, cache)

        placement.pop()
        visited_col.remove(col)
        visited_diagonal_a.remove(row - col)
        visited_diagonal_b.remove(row + col)
        

        

        # self.calcQueenPlace(row, col + 1, placement, prohibited)
        
        # placement.append(place_str)
        # diagonal_right = col + 1
        # diagonal_left = col - 1
        # for next_row in range(row + 1, self.n):
        #     prohibited.add((next_row, col))
        #     if diagonal_right >= 0 and diagonal_right < self.n:
        #         prohibited.add((next_row, diagonal_right))
        #     if diagonal_left >= 0 and diagonal_left < self.n:
        #         prohibited.add((next_row, diagonal_left))
        #     diagonal_right += 1
        #     diagonal_left -= 1

        # self.calcQueenPlace(row + 1, col, placement, prohibited)

        

    # def calculateQueenPlace(self, queen, board_row, board_col, prohibited):
    #     if queen == self.n:
    #         return True
        
    #     if (board_row, board_col) in prohibited:
    #         return False
        
    #     diagonal_right = board_col + 1
    #     diagonal_left = board_col - 1
    #     for row in range(board_row + 1, self.n):
    #         prohibited.add(row, board_col)
    #         if diagonal_right >= 0 and diagonal_right < self.n:
    #             prohibited.add(row, diagonal_right)
    #         if diagonal_left >= 0 and diagonal_left < self.n:
    #             prohibited.add(row, diagonal_left)
    #         diagonal_right += 1
    #         diagonal_left -= 1
        
    #     result = False
    #     for next_col in range(self.n):
    #         result = result or self.CalculateQueenPlace(board_row + 1, next_col, prohibited)
    #     if result