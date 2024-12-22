class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        max_count = 0
        
        for i in nums:
            count[i] = count.get(i, 0) + 1
            max_count = max(max_count, count[i])
        
        freq = [[] for _ in range(max_count + 1)]
        
        for key, val in count.items():
            freq[val].append(key)
        
        res = []
        for i in range(max_count, 0, -1):
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res
        