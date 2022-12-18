class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = dict()
        heap = list()
        
        for p in points:
            d = (p[0] - 0)**2 + (p[1] - 0)**2
            distances[d] = distances.get(d, [])
            distances[d].append(p)
            heap.append(d)
        
        heapq.heapify(heap)
        result = list()
        for _ in range(k):
            for p in distances[heapq.heappop(heap)]:
                if len(result) == k: break
                result.append(p)
        return result