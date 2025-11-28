class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = dict()
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        color = 0
        i = 0
        while i < len(nums):
            if color not in freq:
                color += 1
                continue
            
            nums[i] = color
            freq[color] -= 1
            if freq[color] == 0:
                color += 1
            i += 1
        