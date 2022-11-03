class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_right_height = [[] for _ in range(len(height))]
        max_left, max_right = 0, 0
        result = 0
        
        for i in range(len(height)):
            left = i
            right = len(height) - 1 - i
            max_left_right_height[left].append(max_left)
            max_left_right_height[right].append(max_right)
            
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
        
        for i in range(len(height)):
            total = min(max_left_right_height[i]) - height[i]
            if total > 0: result += total
        
        return result