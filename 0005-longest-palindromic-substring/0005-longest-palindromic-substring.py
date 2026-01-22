class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        result = ""

        for i in range(len(s)):
            isPalindrome, word = self.isPalindrome(i, i)
            if isPalindrome and len(result) < len(word):
                result = word
            
            if i == len(self.s) - 1:
                break

            isPalindrome, word = self.isPalindrome(i, i + 1)
            if isPalindrome and len(result) < len(word):
                result = word
        
        return result

    def isPalindrome(self, left, right):
        if left != right and self.s[left] != self.s[right]:
            return False, ""
        
        word = ""
        while left <= right and left >= 0 and right < len(self.s):
            if self.s[left] != self.s[right]:
                break
            if left == right:
                word = self.s[left]
            else:
                word = self.s[left] + word + self.s[right]

            left -= 1
            right += 1

        return True, word