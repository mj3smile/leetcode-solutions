class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1
        
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            result = max(result, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return result
