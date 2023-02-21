class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        previous_sum = 0
        
        if len(arr) < k:
            return result
        
        previous_sum = sum(arr[:k])
        if previous_sum / k >= threshold:
            result += 1
        
        l = 1
        for r in range(k, len(arr)):
            previous_sum -= arr[l - 1]
            previous_sum += arr[r]
            average = previous_sum / k
            if average >= threshold:
                print(average, l, r)
                result += 1
            l += 1
        
        return result