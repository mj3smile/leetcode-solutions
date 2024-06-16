class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        for i in range(len(nums)):
            left_val = 1
            if i > 0:
                left_val = left[i - 1]
            left[i] = left_val * nums[i]
            
            right_val = 1
            last_index = len(nums) - 1
            curr_index = last_index - i
            if curr_index < last_index:
                right_val = right[curr_index + 1]
            right[curr_index] = right_val * nums[curr_index]
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = right[i + 1]
            elif i == len(nums) - 1:
                result[i] = left[i - 1]
            else:
                result[i] = left[i - 1] * right[i + 1]
        
        return result