class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = list()
        frequency = dict()
        min_frequency = len(nums) // 3

        cache = set()
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            if frequency[n] > min_frequency and n not in cache:
                result.append(n)
                cache.add(n)
        
        return result