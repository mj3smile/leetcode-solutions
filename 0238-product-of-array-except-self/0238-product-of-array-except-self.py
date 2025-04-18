class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = list()
        right_to_left = [0] * len(nums)

        for left in range(len(nums)):
            right = len(nums) - 1 - left

            if left == 0:
                left_to_right.append(nums[left])
                right_to_left[right] = nums[right]
                continue
            
            left_to_right.append(left_to_right[left - 1] * nums[left])
            right_to_left[right] = right_to_left[right + 1] * nums[right]
        
        result = list()
        for i in range(len(nums)):
            left, right = 1, 1
            if i > 0:
                left = left_to_right[i - 1]
            
            if i < len(nums) - 1:
                right = right_to_left[i + 1]
            
            result.append(left * right)
        
        return result
