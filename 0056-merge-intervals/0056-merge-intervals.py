class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        
#         b, f = 0, 1
#         while f < len(intervals):
#             back, front = intervals[b], intervals[f]
#             if front[0] in range(back[0], back[1] + 1):
#                 back[1] = max(back[1], front[1])
#             else:
#                 result.append(back)
#                 b = f
#             f += 1
        
        for i in intervals[1:]:
            first, last = result[-1]
            if i[0] in range(first, last + 1):
                result[-1][1] = max(last, i[1])
            else:
                result.append(i)
                
        # result.append(intervals[b])
        return result
                