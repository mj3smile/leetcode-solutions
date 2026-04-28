class DetectSquares:
    def __init__(self):
        self.xs = dict()
        self.ys = dict()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xs[x] = self.xs.get(x, dict())
        self.xs[x][y] = self.xs[x].get(y, 0) + 1

        self.ys[y] = self.ys.get(y, dict())
        self.ys[y][x] = self.ys[y].get(x, 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point
        if x not in self.xs or y not in self.ys:
            return 0

        result = 0
        for y2 in self.xs[x]:
            result += self.countPossibleSquareBySameX(point, [x, y2])
        return result
    
    def countPossibleSquareBySameX(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        result = 0

        ymax, ymin = y2, y1
        if y1 > y2:
            ymax, ymin = y1, y2

        length = ymax - ymin
        if length == 0:
            return 0

        if x1 - length in self.xs and ymax in self.xs[x1 - length] and ymin in self.xs[x1 - length]:
            result += (self.xs[x1 - length][ymin] * self.xs[x1 - length][ymax] * self.xs[x2][y2])
        
        if x1 + length in self.xs and ymax in self.xs[x1 + length] and ymin in self.xs[x1 + length]:
            result += (self.xs[x1 + length][ymin] * self.xs[x1 + length][ymax] * self.xs[x2][y2])
        
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)