class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        result = 0

        for right in range(len(arr)):
            # print("right:", right)
            # print((arr[right - 1] < arr[right] and (right + 1 == len(arr) or arr[right] > arr[right + 1])))
            # print((arr[right - 1] > arr[right] and (right + 1 == len(arr) or arr[right] < arr[right + 1])))
            # if not ((arr[right - 1] < arr[right] and (right + 1 == len(arr) or arr[right] > arr[right + 1])) or (arr[right - 1] > arr[right] and (right + 1 == len(arr) or arr[right] < arr[right + 1]))):
            #     left = right
            
            if right > 0 and arr[right - 1] == arr[right]:
                left = right
            elif right - 2 >= 0 and ((arr[right] > arr[right - 1] and arr[right - 1] > arr[right - 2]) or (arr[right] < arr[right - 1] and arr[right - 1] < arr[right - 2])):
                left = right - 1
            # if (arr[right] - 1 > arr[right] and (right + 1 == len(arr) or arr[right] < arr[right + 1])):
            result = max(result, right - left + 1)
            
            print("left:", left, 'right:', right)
            
        
        return result