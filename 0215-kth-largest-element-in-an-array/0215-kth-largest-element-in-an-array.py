class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        result = nums[0]
        for _ in range(k):
            result = heapq.heappop(nums)
        return result * -1