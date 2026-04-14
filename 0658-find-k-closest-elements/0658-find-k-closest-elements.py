class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2

            if arr[mid] == x or arr[mid] > x:
                right = mid
            else:
                left = mid + 1
        
        if right > 0 and arr[right] != x and arr[right] - x >= x - arr[right - 1]:
            right -= 1
        
        left, right = right, right
        while right - left + 1 < k and (left >= 0 or right < len(arr)):
            if left - 1 < 0 and right + 1 < len(arr):
                right += 1
            elif left - 1 >= 0 and right + 1 == len(arr):
                left -= 1
            else:
                if arr[right + 1] - x < x - arr[left - 1]:
                    right += 1
                else:
                    left -= 1

        return arr[left:right+1]