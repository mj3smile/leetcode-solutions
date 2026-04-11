class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
        
        heap = []
        heapq.heapify(heap)
        for num, freq in frequencies.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for freq, num in heap:
            result.append(num)
        
        return result
