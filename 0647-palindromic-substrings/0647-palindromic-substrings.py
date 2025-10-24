class Solution:
    def countSubstrings(self, s: str) -> int:
        self.s = s
        self.result = 0
        for i in range(len(s)):
            self.countPalindromeFromCenter(i, i)
            if i < len(s) - 1: self.countPalindromeFromCenter(i, i + 1)
        return self.result

    def countPalindromeFromCenter(self, center_index_left, center_index_right):
        while center_index_left >= 0 and center_index_right < len(self.s) and self.s[center_index_left] == self.s[center_index_right]:
            self.result += 1
            center_index_left -= 1
            center_index_right += 1