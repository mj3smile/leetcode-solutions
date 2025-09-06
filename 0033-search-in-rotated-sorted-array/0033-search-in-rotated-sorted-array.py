class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotated = len(nums) > 1 and nums[0] > nums[-1]
        left, right = 0, len(nums) - 1

        pivot, i = 1, 1
        while rotated and i < len(nums) and nums[i] > nums[0]:
            pivot += 1
            i += 1
        
        if rotated:
            if target < nums[0]:
                left = pivot
            else:
                right = pivot - 1
        
        print(left, right)
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1