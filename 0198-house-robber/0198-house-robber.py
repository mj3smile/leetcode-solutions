class Solution:
    def rob(self, nums: List[int]) -> int:
        visited = set()
        cache = dict()
        def count(n):
            if n >= len(nums):
                return 0
            if n in cache:
                return cache[n]
            
            total = nums[n]
            total += max(count(n + 2), count(n + 3))
            cache[n] = total
            
            return total
        
        return max(count(0), count(1))