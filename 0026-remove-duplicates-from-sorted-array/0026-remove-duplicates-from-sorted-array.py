class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        items = set()

        if nums:
            items.add(nums[0])

        for right in range(1, len(nums)):
            if nums[right] > nums[left - 1] and left < right:
                nums[left] = nums[right]
                left += 1
            items.add(nums[right])
        
        return len(items)