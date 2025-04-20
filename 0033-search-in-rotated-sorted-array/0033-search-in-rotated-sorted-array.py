class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        if nums[right] < nums[left]:
            pivot = right
            while nums[pivot] >= nums[pivot - 1]:
                pivot -= 1
            
            if target <= nums[right]:
                left = pivot
            else:
                right = pivot - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1