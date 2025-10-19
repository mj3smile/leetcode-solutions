class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_to_left_prefix = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_to_left_prefix[i] = right_to_left_prefix[i + 1] * nums[i]
        
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(right_to_left_prefix[i + 1])
                continue
            if i == len(nums) - 1:
                result.append(nums[i - 1])
                continue
            
            nums[i] *= nums[i - 1]
            result.append(nums[i - 1] * right_to_left_prefix[i + 1])
        
        return result