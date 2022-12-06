class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         result = False
        
#         def jump(i):
#             nonlocal result
#             if result:
#                 return
            
#             if i == len(nums) - 1:
#                 result = True
#                 return
            
#             if i >= len(nums) or nums[i] == 0:
#                 return
            
#             # max_jump = nums[i]
#             while nums[i] > 0 and not result:
#                 jump(i + nums[i])
#                 nums[i] -= 1
#             # jump(i + 1)
        
#         jump(0)
        
        target = len(nums) - 1
        result = True
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
                result = True
            else:
                result = False
        
        return result