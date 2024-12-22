class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements  = dict()   # k: element of nums, v: frequency
        frequency = dict()   # k: frequency, v: element of nums

        for n in nums:
            elements[n] = elements.get(n, 0) + 1
            frequency[elements[n]] = n
        
        print(frequency)
        sorted_frequencies = sorted(frequency.keys())
        result = list()
        for i in range(len(frequency) - k, len(frequency)):
            f = sorted_frequencies[i]
            result.append(frequency[f])

        return result