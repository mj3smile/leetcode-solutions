class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            sorted_subarr = []
            p1, p2 = l, m + 1
            while p1 <= m and p2 <= r:
                if arr[p1] <= arr[p2]:
                    sorted_subarr.append(arr[p1])
                    p1 += 1
                else:
                    sorted_subarr.append(arr[p2])
                    p2 += 1
            if p1 <= m: sorted_subarr += arr[p1:m + 1]
            if p2 <= r: sorted_subarr += arr[p2:r + 1]
            
            m = 0
            for i in range(l, r + 1):
                arr[i] = sorted_subarr[m]
                m += 1
            
        def divide(arr, l, r):
            if r - l + 1 == 1:
                return
            
            m = (l + r) // 2
            divide(arr, l, m)
            divide(arr, m + 1, r)
            merge(arr, l, m, r)
        
        divide(nums, 0, len(nums) - 1)
        return nums