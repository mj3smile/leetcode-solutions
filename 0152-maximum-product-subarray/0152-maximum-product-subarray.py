class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]

        min_product, max_product = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                result = max(result, nums[i])
                min_product, max_product = 1, 1
                continue
            
            total_1, total_2 = min_product * nums[i], max_product * nums[i]
            max_product = max(total_1, total_2, nums[i])
            min_product = min(total_1, total_2, nums[i])
            
            result = max(result, max_product)
        
        return result