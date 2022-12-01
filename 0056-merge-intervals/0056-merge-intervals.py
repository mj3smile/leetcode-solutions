class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        
        for i in intervals[1:]:
            first, last = result[-1]
            if i[0] <= last:
                result[-1][1] = max(last, i[1])
            else:
                result.append(i)

        return result
                