class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        if left == right or nums[left] < nums[right]:
            return nums[0]
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        