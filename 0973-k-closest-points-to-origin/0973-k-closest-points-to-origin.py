class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = list()
        heapq.heapify(heap)

        for x1, y1 in points:
            heapq.heappush(heap, [self.distance(x1, y1, 0, 0), [x1, y1]])
        
        result = list()
        for _ in range(k):
            p = heapq.heappop(heap)[1]
            result.append(p)
            
        return result

    def distance(self, x1, y1, x2, y2):
        result = (x1 - x2)**2 + (y1 - y2)**2
        result = result**0.5
        return result