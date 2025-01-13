class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        left = 0
        window_cache = dict()
        for right in range(len(s)):
            while s[right] in window_cache and left <= window_cache[s[right]]:
                del window_cache[s[left]]
                left += 1
            
            result = max(result, right - left + 1)
            window_cache[s[right]] = right
        
        return result