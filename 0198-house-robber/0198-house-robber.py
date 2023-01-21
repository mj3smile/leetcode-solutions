class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        counts = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            tmp = counts[1]
            counts[1] = nums[i] + counts[0]
            counts[0] = max(tmp, counts[0])
        
        return max(counts)
    

#         visited = set()
#         cache = dict()
#         def count(n):
#             if n >= len(nums):
#                 return 0
#             if n in cache:
#                 return cache[n]
            
#             total = nums[n]
#             total += max(count(n + 2), count(n + 3))
#             cache[n] = total
            
#             return total
        
#         return max(count(0), count(1))