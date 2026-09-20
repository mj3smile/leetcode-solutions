class Solution:
    def merge(self, original, arr1, arr2):
        j, k = 0, 0
        for i in range(len(original)):
            if k >= len(arr2) or j < len(arr1) and arr1[j] <= arr2[k]:
                original[i] = arr1[j]
                j += 1
            else:
                original[i] = arr2[k]
                k += 1

    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return nums
        
        start, end = 0, len(nums)
        mid = (start + end) // 2

        half1 = self.sortArray(nums[start:mid])
        half2 = self.sortArray(nums[mid:end])

        self.merge(nums, half1, half2)
        return nums