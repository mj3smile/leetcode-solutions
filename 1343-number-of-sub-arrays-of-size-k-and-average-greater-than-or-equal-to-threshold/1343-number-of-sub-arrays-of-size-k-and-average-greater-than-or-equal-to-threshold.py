class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        previous_sum = sum(arr[:k - 1])
        
        for i in range(len(arr) - k + 1):
            left, right = i, i + k - 1
            previous_sum += arr[right]
            if previous_sum / k >= threshold:
                result += 1
            previous_sum -= arr[left]
        
        return result