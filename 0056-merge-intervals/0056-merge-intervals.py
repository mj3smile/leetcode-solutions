class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        
        b, f = 0, 1
        while f < len(intervals):
            back, front = intervals[b], intervals[f]
            if not front[0] in range(back[0], back[1] + 1):
                result.append(back)
                b = f
            else:
                back[0] = min(back[0], front[0])
                back[1] = max(back[1], front[1])
            f += 1
            
        result.append(intervals[b])
        return result
                