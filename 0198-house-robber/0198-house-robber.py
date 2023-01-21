class Solution:
    def rob(self, nums: List[int]) -> int:
        counts = [0] * len(nums)
        
        for i in range(len(nums)):
            first = 0 if i - 3 < 0 else counts[i - 3]
            second = 0 if i - 2 < 0 else counts[i - 2]
            counts[i] = nums[i] + max(first, second)
        
        print(counts)
        return counts[-2] if len(nums) >= 2 and counts[-2] > counts[-1] else counts[-1]
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