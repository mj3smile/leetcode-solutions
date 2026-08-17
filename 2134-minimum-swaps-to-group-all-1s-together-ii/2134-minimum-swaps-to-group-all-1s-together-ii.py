class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        prefix_sum = [0 for _ in range(len(nums))]
        area = 0

        for i in range(len(nums)):
            if i > 0:
                prefix_sum[i] = prefix_sum[i - 1]
            if nums[i] == 1:
                prefix_sum[i] += 1
                area += 1
        
        max_1_in_area = 0
        for i in range(len(nums)):
            start, end = i, i + (area - 1)
            count = 0
            print(start, end)
            if end >= len(nums):
                count += prefix_sum[end - len(nums)]
                # print("e", end, count)
                end = len(nums) - 1

            count += prefix_sum[end]
            if start > 0:
                count -= prefix_sum[start - 1]
            
            # print(start, end, count)
            max_1_in_area = max(max_1_in_area, count)
        
        return area - max_1_in_area
            
