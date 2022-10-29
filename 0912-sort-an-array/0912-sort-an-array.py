class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            first, second = arr[l:m + 1].copy(), arr[m + 1:r + 1].copy()
            n1, n2 = len(first), len(second)
            p1, p2, p3 = 0, 0, l
            while p3 <= r and (p1 < n1 or p2 < n2):
                if p2 >= n2 and p1 < n1:
                    arr[p3] = first[p1]
                    p1, p3 = p1 + 1, p3 + 1
                    continue
                    
                if p1 >= n1 and p2 < n2:
                    arr[p3] = second[p2]
                    p2, p3 = p2 + 1, p3 + 1
                    continue
                
                if first[p1] <= second[p2]:
                    arr[p3] = first[p1]
                    p1 += 1
                else:
                    arr[p3] = second[p2]
                    p2 += 1
                p3 += 1
                
            
        def divide(arr, left, right):
            if right - left + 1 == 1:
                return
            
            middle = (left + right) // 2
            divide(arr, left, middle)
            divide(arr, middle + 1, right)
            merge(arr, left, middle, right)
        
        divide(nums, 0, len(nums) - 1)
        return nums