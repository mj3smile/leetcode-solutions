class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = list()
        queue = deque()

        max_num = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] > nums[max_num]:
                max_num = right
            
            if len(queue) == 0 or queue[-1] > nums[right]:
                queue.append(nums[right])
            else:
                queue.pop()
                queue.append(nums[right])

            if right - left + 1 < k:
                continue
            
            result.append(nums[max_num])
            left += 1

            if left > max_num:
                queue.popleft()
        
        return result

            