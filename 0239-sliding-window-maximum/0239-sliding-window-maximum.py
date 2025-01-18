class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = list()
        queue = deque()

        left = 0
        for right in range(len(nums)):
            if len(queue) == 0 or nums[queue[-1]] > nums[right]:
                queue.append(right)
            else:
                while len(queue) > 0 and nums[queue[-1]] < nums[right]:
                    queue.pop()
                queue.append(right)

            if right - left + 1 < k:
                continue
            
            result.append(nums[queue[0]])
            if left + 1 > queue[0]:
                queue.popleft()
            
            left += 1
        
        return result

            