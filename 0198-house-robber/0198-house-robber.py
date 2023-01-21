class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 1
        visited = set()
        cache = dict()
        def count(n):
            if n >= len(nums):
                return 0
            if n in cache:
                return cache[n]
            
            visited.add(n)
            total = nums[n]
            total += max(count(n + 2), count(n + 3))
            visited.remove(n)
            cache[n] = total
            
            return total
        
        return max(count(r1), count(r2))