class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        result = 0
        i = 0
        while i < len(points):
            s, e = points[i]

            j = i + 1
            while j < len(points) and s <= points[j][0] <= e:
                s = max(s, points[j][0])
                e = min(e, points[j][1])
                j += 1

            i = j     
            result += 1
        
        return result