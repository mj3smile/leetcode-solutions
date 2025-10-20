class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = len(result)

        for i in range(len(s)):
            odd = self.getPalindromeSubstring(i, i)
            if len(odd) > result_len:
                result, result_len = odd, len(odd)

            even = self.getPalindromeSubstring(i, i + 1)
            if len(even) > result_len:
                result, result_len = even, len(even)
        
        return result

    def getPalindromeSubstring(self, left, right):
        result = ""
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            result = self.s[left] + result
            if left != right: result += self.s[right]
            left -= 1
            right += 1

        return result