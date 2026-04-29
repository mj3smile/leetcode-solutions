class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(start, end):
            result = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                result += 1
                start -= 1
                end += 1
            return result
        
        result = 0
        for i in range(len(s)):
            result += countPalindrome(i, i)
            if i + 1 < len(s):
                result += countPalindrome(i, i + 1)
        
        return result