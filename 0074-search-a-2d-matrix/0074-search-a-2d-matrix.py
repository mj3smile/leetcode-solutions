class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        
        while top <= bottom:
            middle = (top + bottom) // 2
            
            if target > matrix[middle][-1]:
                top = middle + 1
                continue
            elif target < matrix[middle][0]:
                bottom = middle - 1
                continue
            
            target_list = matrix[middle]
            left, right = 0, len(target_list) - 1
            while left <= right:
                middle = (left + right) // 2
                
                if target == target_list[middle]:
                    return True
                elif target > target_list[middle]:
                    left = middle + 1
                elif target < target_list[middle]:
                    right = middle - 1
            
            return False
        
        return False