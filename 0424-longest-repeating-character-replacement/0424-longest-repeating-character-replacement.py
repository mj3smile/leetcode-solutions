class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        counts = dict()
        
        l = 0
        most_freq = s[0]
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            if counts[s[r]] > counts[most_freq]:
                most_freq = s[r]
            
            if (r - l + 1) - counts[most_freq] > k:
                counts[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result