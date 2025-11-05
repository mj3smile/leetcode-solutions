class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        left = 0
        curSum = 0

        for right in range(len(arr)):
            if right - left + 1 > k:
                curSum -= arr[left]
                left += 1
            
            curSum += arr[right]
            if right - left + 1 == k and curSum // k >= threshold:
                result += 1
        
        return result