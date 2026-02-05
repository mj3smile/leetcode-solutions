class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightToLeftProduct = [nums[-1] for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            rightToLeftProduct[i] = nums[i] * rightToLeftProduct[i + 1]
        
        result = list()
        prefix = 1
        for i in range(len(nums)):
            suffix = 1
            if i < len(nums) - 1:
                suffix = rightToLeftProduct[i + 1]
            result.append(prefix * suffix)
            prefix *= nums[i]
        
        return result
