class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        previous_sum = sum(arr[:k])
        
        l = 1
        for r in range(k, len(arr) + 1):
            if previous_sum / k >= threshold:
                result += 1
            if r == len(arr):
                break
                
            previous_sum -= arr[l - 1]
            previous_sum += arr[r]
            l += 1
        
        return result