class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
        
        print(frequencies)

        heap = list()
        heapq.heapify(heap)
        heap_size = 0
        for num, frequency in frequencies.items():
            heapq.heappush(heap, (frequency, num))
            heap_size += 1

            if heap_size > k:
                heapq.heappop(heap)
        
        result = list()
        for _ in range(k):
            frequency, num = heapq.heappop(heap)
            result.append(num)
        
        return result