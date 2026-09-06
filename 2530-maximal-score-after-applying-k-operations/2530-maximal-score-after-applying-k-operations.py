class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        result = 0

        while k > 0:
            if not nums:
                break
            max_num = heapq.heappop_max(nums)
            result += max_num
            addition = 0
            if max_num % 3 > 0:
                addition = 1

            heapq.heappush_max(nums, max_num // 3 + addition)
            k -= 1
        
        return result