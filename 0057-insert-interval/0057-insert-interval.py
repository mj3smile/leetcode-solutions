class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if not intervals: return [newInterval]
        # left, right = 0, len(intervals) - 1

        # insertPoint = 0
        # while left < right:
        #     mid = (left + right) // 2

        #     if intervals[mid][0] == newInterval[0]:
        #         left = mid
        #         break
        #     elif intervals[mid][0] > newInterval[0]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # insertPoint = left
        # if left > 0 and intervals[left][0] > newInterval[0]:
        #     insertPoint = left -1

        # print(insertPoint)
        # result = list()
        # i = 0
        # while i < len(intervals):
        #     if i == insertPoint:
        #         if intervals[i][1] < newInterval[0] and (i == len(intervals) - 1 or intervals[i + 1][0] > newInterval[1]):
        #             result.append(intervals[i])
        #             result.append(newInterval)
        #         else:
        #             newStart = min(intervals[i][0], newInterval[0])
        #             while i + 1 < len(intervals) and intervals[i][1] < newInterval[1] and intervals[i + 1][0] <= newInterval[1]:
        #                 i += 1
        #             newEnd = max(intervals[i][1], newInterval[1])
        #             result.append([newStart, newEnd])
        #     else:
        #         result.append(intervals[i])
        #     i += 1
        
        # return result

        i = 0
        result = list()
        merged = False
        while i < len(intervals):
            if merged or intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
                i += 1
            elif newInterval[1] < intervals[i][0]:
                merged = True
                result.append(newInterval)
            else:
                merged = True
                newStart = min(intervals[i][0], newInterval[0])
                while i + 1 < len(intervals) and intervals[i + 1][0] <= newInterval[1]:
                    i += 1
                newEnd = max(intervals[i][1], newInterval[1])
                result.append([newStart, newEnd])
                i += 1
        if not merged:
            result.append(newInterval)
        return result

