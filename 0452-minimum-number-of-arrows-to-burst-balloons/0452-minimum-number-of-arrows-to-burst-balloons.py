class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        result = 0
        i = 0
        while i < len(points):
            s, e = points[i]

            i = i + 1
            while i < len(points) and s <= points[i][0] <= e:
                s = max(s, points[i][0])
                e = min(e, points[i][1])
                i += 1

            result += 1
        
        return result