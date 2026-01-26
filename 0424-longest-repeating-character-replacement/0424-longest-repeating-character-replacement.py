class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        charFreq = dict()
        maxCharFreq = 0
        left = 0
        for right in range(len(s)):
            charFreq[s[right]] = charFreq.get(s[right], 0) + 1
            maxCharFreq = max(maxCharFreq, charFreq[s[right]])
            
            while (right - left + 1) - maxCharFreq > k:
                charFreq[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
