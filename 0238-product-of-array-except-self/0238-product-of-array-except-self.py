class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * (len(nums) + 2)
        right = [1] * (len(nums) + 2)
        
        for i in range(len(nums)):
            left[i + 1] = left[i] * nums[i]
            right[len(nums) - i] = right[len(nums) - i + 1] * nums[len(nums) - i - 1]
        
        result = [0] * (len(nums) + 2)
        for i in range(1, len(result) - 1):
            if i == 1:
                result[i] = right[i + 1]
            elif i == len(result) - 2:
                result[i] = left[i - 1]
            else:
                result[i] = left[i - 1] * right[i + 1]
        
        return result[1:-1]