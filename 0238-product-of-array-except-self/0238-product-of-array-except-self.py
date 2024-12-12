class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right_multiplication = [0] * len(nums)
        right_to_left_multiplication = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                left_to_right_multiplication[i] = nums[i]
                continue
            
            left_to_right_multiplication[i] = nums[i] * left_to_right_multiplication[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_to_left_multiplication[i] = nums[i]
                continue
            
            right_to_left_multiplication[i] = nums[i] * right_to_left_multiplication[i + 1]
        
        result = list()
        for i in range(len(nums)):
            if i == 0:
                result.append(right_to_left_multiplication[i + 1])
                continue
            
            if i == len(nums) - 1:
                result.append(left_to_right_multiplication[i - 1])
                continue
            
            result.append(left_to_right_multiplication[i - 1] * right_to_left_multiplication[i + 1])
        
        return result
