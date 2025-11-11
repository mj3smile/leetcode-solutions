class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        rotated = nums[-1] < nums[0]
        while rotated and nums[left] > nums[right]:
            left += 1
        return nums[left]