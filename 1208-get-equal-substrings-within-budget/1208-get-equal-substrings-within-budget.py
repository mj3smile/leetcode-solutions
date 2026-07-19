class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        prefix_sum = {-1: 0}
        for i in range(len(s)):
            diff = ord(s[i]) - ord(t[i])
            if diff < 0:
                diff = -diff
            prefix_sum[i] = diff + prefix_sum[i - 1]
        
        l = 0
        result = 0
        for r in range(len(s)):
            while prefix_sum[r] - prefix_sum[l - 1] > maxCost:
                l += 1
            
            result = max(result, r - l + 1)
        
        return result