class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        heap = list()
        heapq.heapify(heap)
        for i in range(len(temperatures)):
            while heap and heap[0][0] < temperatures[i]:
                pastTemp, index = heapq.heappop(heap)
                result[index] = i - index
            heapq.heappush(heap, (temperatures[i], i))
        return result