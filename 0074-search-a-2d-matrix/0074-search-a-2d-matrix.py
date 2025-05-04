class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        found = False

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                found = True
                left = mid
                break
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1
        
        if not found:
            return False
        
        row = matrix[left]
        left, right = 0, len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif target > row[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False