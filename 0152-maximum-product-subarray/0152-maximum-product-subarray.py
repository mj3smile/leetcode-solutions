class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        leftCurr = 1
        rightCurr = 1

        for i in range(len(nums)):
            leftCurr *= nums[i]
            rightCurr *= nums[len(nums) - 1 - i]
            result = max(result, leftCurr)
            result = max(result, rightCurr)

            if nums[i] == 0:
                leftCurr = 1
            if nums[len(nums) - 1 - i] == 0:
                rightCurr = 1
        
        return result