class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list()
        heapq.heapify(heap)
        for s in stones:
            heapq.heappush(heap, -s)

        while heap:
            heaviest = heapq.heappop(heap) * -1
            if not heap:
                return heaviest
            secondHeaviest = heapq.heappop(heap) * -1
            heapq.heappush(heap, (heaviest - secondHeaviest) * -1)