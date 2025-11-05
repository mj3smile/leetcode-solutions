class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums)
        found = False
        left = 0
        curSum = 0

        for right in range(len(nums)):
            curSum += nums[right]

            while curSum >= target:
                print(f"left: {left}, right: {right}, curSum: {curSum}")
                found = True
                result = min(result, right - left + 1)
                curSum -= nums[left]
                left += 1
        
        if not found: return 0
        return result