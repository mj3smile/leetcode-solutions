class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        # result = arr[0]
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i] - (arr[i] - arr[i - 1] - 1)
                # result = max(result, arr[i])
        print(arr)
        return max(arr)