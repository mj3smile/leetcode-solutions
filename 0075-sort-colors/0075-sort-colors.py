class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0 for _ in range(3)]
        for i in nums:
            bucket[i] += 1
        
        j = 0
        for i in range(len(bucket)):
            for _ in range(bucket[i]):
                nums[j] = i
                j += 1