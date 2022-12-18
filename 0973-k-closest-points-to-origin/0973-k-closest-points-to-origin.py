import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda x: (x[0] - 0)**2 + (x[1] - 0)**2)
        return points[:k]