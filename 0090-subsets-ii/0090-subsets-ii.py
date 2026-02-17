class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        freqIndex = dict()
        freq = list()
        for n in nums:
            if n in freqIndex:
                continue
            freqIndex[n] = len(freq)
            freq.append(0)
        
        result = list()
        cache = set()
        def subset(index, currSubset, freq):
            if index == len(nums):
                key = tuple(freq)
                if key in cache: return
                result.append(currSubset.copy())
                cache.add(key)
                return
            
            for i in range(index, len(nums)):
                currSubset.append(nums[i])
                freq[freqIndex[nums[i]]] += 1
                subset(i + 1, currSubset, freq)
                freq[freqIndex[nums[i]]] -= 1
                currSubset.pop()

                subset(i + 1, currSubset, freq)
        
        subset(0, list(), freq)
        return result