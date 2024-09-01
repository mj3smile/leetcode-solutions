class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[0] > nums[-1]:
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    continue
                
                if target < nums[left]:
                    left = i + 1
                else:
                    right = i
                    
                break
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1